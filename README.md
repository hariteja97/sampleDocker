# Neo4j docker for data science purpose.
Docker template for basic data science packages to interface with Neo4j

## Introduction

This container is based on the Juptyer lab container along side with  a Neo4j database on your local machine. This container does NOT include support for GPU-based deep learning packages (Try to explore more on the how gpu can be used). There might be few unncessary packages.  It is more of a generic container to get you started.

## To run this container

First, build the container from the CLI:

```
docker-compose build
```

Then start the container:

```
docker-compose up
```

This will start up both a Jupyter Lab notebook at `localhost:8888`(sometimes it might ask for a the session key of the jupyter notebook to keep track) as well as the Neo4j browser at `localhost:7474`.  This are both configurable to whatever port you want.

When you are done with the container, stop it vial `CTRL-c` and then:

```
docker-compose down
```

## Some notes

- There are two different Python packages that can be used to connect to Neo4j from within Python.  It is probably easiest to just pick one and go with it.
  - `neo4j`(https://neo4j.com/docs/api/python-driver/current/): The official, Neo4j-supported Python driver
  - `py2neo`(https://py2neo.org/2021.0/): A community-developed driver with lots of solid documentation and examples out there
  - '
- The container is set up to run Neo4j with the user name `neo4j` and the password as `1234`. Please feel free to change the password for your own purpose.
- There is a notebook in `notebooks/` that tests to make sure that Jupyter can properly connect to Neo4j.  Run this to verify.
- The `docker-compose.yml` is set to create and read data into Neo4j (including creating the database itself) in the directory `$HOME/graph_data/my_data`.  You should change this to whatever directory you want to store the database.  You will also use these directorys should you want to read `.csv` files into the database.
- The `docker-compose.yml` file includes some optional environment variables for setting memory values.  Since this container includes the Graph Data Science (GDS) library, it is a good idea to add some heap memory(I didn't add them on purpose for your learning and exploration).  The exact values will depend on your machine.  You will want to experiment with tuning this based on [these instructions](https://neo4j.com/docs/operations-manual/current/performance/memory-configuration/)
- The Neo4j portion of the container includes two libraries that are very helpful for doing data science with graphs.  These are APOC and GDS.  The latest versions should be pulled when this container executes.  Links to their use are provided below.

## Some helpful links

- [Neo4j](https://neo4j.com)
  - [Awesome Procedures on Cypher (APOC)](https://neo4j.com/labs/apoc/)
  - [Cypher Manual](https://neo4j.com/docs/cypher-manual/current/)
  - [Cypher Reference Card](https://neo4j.com/docs/pdf/neo4j-cypher-refcard-stable.pdf)
  - [Graph Data Science (GDS) Library](https://neo4j.com/developer/graph-data-science/)
  - [Python Driver API Docs](https://neo4j.com/docs/api/python-driver/current/)
  - [Neo4j with Docker](https://neo4j.com/developer/docker-run-neo4j/)
  - [Docker compose Documentation for GPU setup](https://docs.docker.com/compose/gpu-support/)

