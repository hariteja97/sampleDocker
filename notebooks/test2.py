from neo4j import GraphDatabase

import os
import time
URL=os.getenv('NEO4J_URI')
driver = GraphDatabase.driver(URL,auth=("neo4j", "password"))
def function():

    def add_friend(tx, name, friend_name):
        tx.run("MERGE (a:Person {name: $name}) "
               "MERGE (a)-[:KNOWS]->(friend:Person {name: $friend_name})",
               name=name, friend_name=friend_name)

    def print_friends(tx, name):
        query = ("MATCH (a:Person)-[:KNOWS]->(friend) WHERE a.name = $name "
                 "RETURN friend.name ORDER BY friend.name")
        for record in tx.run(query, name=name):
            print(record["friend.name"])

    with driver.session(database="neo4j") as session:
        session.execute_write(add_friend, "Arthur", "Guinevere")
        session.execute_write(add_friend, "Arthur", "Lancelot")
        session.execute_write(add_friend, "Arthur", "Merlin")
        session.execute_read(print_friends, "Arthur")

    driver.close()

if __name__ == "__main__":
    time.sleep(25)
    function()