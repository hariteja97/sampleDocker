from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
    UniqueIdProperty, RelationshipTo)
import pandas as pd
import numpy as np
import sys
import os
import time

config.DATABASE_URL = os.getenv('NEO4J_URI')


def function():
    class Country(StructuredNode):
        code = StringProperty(unique_index=True, required=True)

    class Person(StructuredNode):
        uid = UniqueIdProperty()
        name = StringProperty(unique_index=True)
        age = IntegerProperty(index=True, default=0)

        # traverse outgoing IS_FROM relations, inflate to Country objects
        country = RelationshipTo(Country, 'IS_FROM')

    ##Create,update,delete operations
    print("Connection URL used:", os.getenv('NEO4J_URI'))
    jim = Person(name='Jim', age=3).save() # Create
    jim.age = 4
    jim.save() # Update, (with validation)
    jim.delete()
    jim.refresh() # reload properties from the database
    jim.id # neo4j internal id

    ## retrieving nodes
    # Return all nodes
    all_nodes = Person.nodes.all()
    print("Print all nodes present,", all_nodes)

    # Returns Person by Person.name=='Jim' or raises neomodel.DoesNotExist if no match
    jim = Person.nodes.get(name='Jim')

    ## search
    # Will return None unless "bob" exists
    someone = Person.nodes.get_or_none(name='bob')
    print("Search for bob",someone)

    # Will return the first Person node with the name bob. This raises neomodel.DoesNotExist if there's no match.
    someone = Person.nodes.first(name='bob')

    # Will return the first Person node with the name bob or None if there's no match
    someone = Person.nodes.first_or_none(name='bob')

    # Return set of nodes
    people = Person.nodes.filter(age__gt=3)

    ##creating relationships
    germany = Country(code='DE').save()
    jim.country.connect(germany)

    if jim.country.is_connected(germany):
        print("Jim's from Germany")

    for p in germany.inhabitant.all():
        print(p.name) # Jim

    print("Number of inhabitants in Germany-->",len(germany.inhabitant))
    # len(germany.inhabitant) # 1

    # Find people called 'Jim' in germany
    germany.inhabitant.search(name='Jim')

    # Find all the people called in germany except 'Jim'
    germany.inhabitant.exclude(name='Jim')

    # Remove Jim's country relationship with Germany
    jim.country.disconnect(germany)

    usa = Country(code='US').save()
    jim.country.connect(usa)
    jim.country.connect(germany)

    # Remove all of Jim's country relationships
    jim.country.disconnect_all()

    jim.country.connect(usa)
    # Replace Jim's country relationship with a new one
    jim.country.replace(germany)

if __name__ == "__main__":
    time.sleep(25)
    function()
    

'''
neo4j-service:
    container_name: neo4j-service
    build: 
      dockerfile: Dockerfile
      context: ./python
    tty: true
    hostname: neo4j-service
    depends_on:
      - storage
        #condition: service_healthy
    ports:
      - "3000:3000"
    restart:
      always
    networks:
      - lan
    links:
      - storage
    depends_on:
      - storage
    environment:
      NEO4J_URI: bolt://neo4j:password@localhost:7687
      NEO4J_USER: "neo4j"
      PYTHONUNBUFFERED: 1'''