from neo4j import GraphDatabase,basic_auth
from py2neo import Graph
import pandas as pd
import numpy as np
import sys
import os
import time

# def custom_resolver(socket_address):
#     if socket_address == ("localhost", 7687):
#         yield "::1", 7687
#         yield "127.0.0.1", 7687
#     else:
#         from socket import gaierror
#         raise gaierror("Unexpected socket address %r" % socket_address)

def function():
	print("Entereing the main function")
	url="bolt://neo4j:password@localhost:7687" #os.getenv("NEO4J_URI")      #r"bolt://localhost:7687"
	url=os.getenv('NEO4J_URI')
	print("Checking the URL retrieved---> ", url)
	driver = GraphDatabase.driver(url,auth=basic_auth("neo4j","password"))
	
	

	

	'''
	Creating a new record for a movie
	The below following commands are do:
	1. Create a new movie node named as " Die Hard" with its released Date and tagline of the movie
	2. Creates another Person node and it is assigned a Role with different relationships such as Director,Producer. 
	if the relationship is given as acted_in we assign a label to the person as the name of the person in the movie.
	'''

	q1=''' CREATE (DieHard:Movie {title:'Die Hard', released:1988, tagline:'On a good day he is a great cop'})'''
	q_10="""CREATE (Bruce:Person {name:'Bruce Willis', born:1955})-[:ACTED_IN {roles:['John McClane']}]->(DieHard:Movie {title:'Die Hard', released:1988, tagline:'On a good day he is a great cop'})"""

	q_11=""" CREATE (Alan:Person {name:'Alan Rickman', born:1946})-[:ACTED_IN {roles:['Hans Gruber']}]->(DieHard:Movie {title:'Die Hard', released:1988, tagline:'On a good day he is a great cop'}) """

	q_12="""CREATE (Bonnie:Person {name:'Bonnie Bedelia', born:1948})-[:ACTED_IN {roles:['Holly Gennaro McClane']}]->(DieHard:Movie {title:'Die Hard', released:1988, tagline:'On a good day he is a great cop'}) """
	q_13="""CREATE (Regi:Person {name:'Reginald VelJohnson', born:1952})-[:ACTED_IN {roles:['Sgt. AL Powell']}]->(DieHard:Movie {title:'Die Hard', released:1988, tagline:'On a good day he is a great cop'})"""
	q_14="""CREATE (John:Person {name:'John McTiernan', born:1951})-[:DIRECTED]->(DieHard:Movie {title:'Die Hard', released:1988, tagline:'On a good day he is a great cop'})"""
	q_15="""CREATE (JoelS:Person {name:'Joel Silver', born:1952})-[:PRODUCED]->(DieHard:Movie {title:'Die Hard', released:1988, tagline:'On a good day he is a great cop'})"""
	q_16="""CREATE (Lawrence:Person {name:'Lawrence Gordon', born:1936})-[:PRODUCED]->(DieHard:Movie {title:'Die Hard', released:1988, tagline:'On a good day he is a great cop'})"""

	'''
		For inserting the data into the movie table I have created a list of queries which will attach few details about the cast/director/producer
		to the movie.
	'''
	list_q=[q1,q_10,q_11,q_12,q_13,q_14,q_15,q_16]

	'''
	Retrieving some of the movies pertaining to a certain actor

	'''

	c_q1='''
	MATCH (movie:Movie) where{name:"Tom Hanks"}) RETURN movie.title LIMIT 5
	'''

	c_q2='''
	MATCH (nineties:Movie) WHERE nineties.released >= 1990 AND nineties.released < 2000 RETURN nineties.title as MovieTitle,nineties.released as Released
	'''
	c_q3='''
	MATCH (bruce:Person {name: "Bruce Willis"})-[:ACTED_IN]->(bruceMovies) RETURN bruce,bruceMovies
	'''

	'''
	Delete all nodes and relationships from the graph database
	and to check if all nodes are disconnected or not


	'''
	delete_query=''' MATCH (n) DETACH DELETE n'''
	check_query=''' Match (n) return n '''

	lq=[]




	print("Session is beginning")
	with driver.session(database="neo4j") as session:
		print("Session Started")
		
		# for query in list_q:
		# 	try:
	  	# 		session.execute_write(lambda tx: tx.run(query))
		# 	except:
	  	# 		print("Error in uploading a new information")
		
		
		# results = session.execute_read(lambda tx: tx.run(c_q3).data())
		# df_movies=pd.DataFrame()
		
		# for record in results:
		# 	print("Movie Title {} ,--> Release Date: {}".format(record['bruceMovies']['title'],record['bruceMovies']['released']))

		
		movieresults = session.execute_read(lambda tx: tx.run(c_q2).data())
		list_title=[]
		list_released=[]
		for r in movieresults:
			list_title.append(str(r['MovieTitle']))
			list_released.append(int(r['Released']))
			
		df_movies['Title']=list_title
		df_movies['ReleaseYear']=list_released	
		print("Movie Title that release between 1990 and 2000")
		print("*"*50)
		print(df_movies)
		print("*"*50)

		"""
		Delete Operation
		"""
		# try:
		# 	session.execute_write(lambda tx: tx.run(delete_query))
		# except:
		# 	print("Delete operation was not successfull")
		# finally:
		# 	check_r=session.execute_read(lambda tx: tx.run(check_query).data())
		# 	if len(check_r)==0:
		# 		print("Delete operation is done!!")





	driver.close()




if __name__ == "__main__":
	time.sleep(25)
	function()
	


































# from neo4j import GraphDatabase,basic_auth
# from py2neo import Graph
# import pandas as pd
# import numpy as np
# import sys
# import os
# import time

# # def custom_resolver(socket_address):
# #     if socket_address == ("localhost", 7687):
# #         yield "::1", 7687
# #         yield "127.0.0.1", 7687
# #     else:
# #         from socket import gaierror
# #         raise gaierror("Unexpected socket address %r" % socket_address)

# def function():
# 	print("Entereing the main function")
# 	url= os.getenv("NEO4J_URI")      #r"bolt://localhost:7687"
# 	print("Checking the URL retrieved---> ", url)
# 	driver = GraphDatabase(url)


	

# 	'''
# 	Creating a new record for a movie
# 	The below following commands are do:
# 	1. Create a new movie node named as " Die Hard" with its released Date and tagline of the movie
# 	2. Creates another Person node and it is assigned a Role with different relationships such as Director,Producer. 
# 	if the relationship is given as acted_in we assign a label to the person as the name of the person in the movie.
# 	'''

# 	q1=''' CREATE (DieHard:Movie {title:'Die Hard', released:1988, tagline:'On a good day he is a great cop'})'''
# 	q_10="""CREATE (Bruce:Person {name:'Bruce Willis', born:1955})-[:ACTED_IN {roles:['John McClane']}]->(DieHard:Movie {title:'Die Hard', released:1988, tagline:'On a good day he is a great cop'})"""

# 	q_11=""" CREATE (Alan:Person {name:'Alan Rickman', born:1946})-[:ACTED_IN {roles:['Hans Gruber']}]->(DieHard:Movie {title:'Die Hard', released:1988, tagline:'On a good day he is a great cop'}) """

# 	q_12="""CREATE (Bonnie:Person {name:'Bonnie Bedelia', born:1948})-[:ACTED_IN {roles:['Holly Gennaro McClane']}]->(DieHard:Movie {title:'Die Hard', released:1988, tagline:'On a good day he is a great cop'}) """
# 	q_13="""CREATE (Regi:Person {name:'Reginald VelJohnson', born:1952})-[:ACTED_IN {roles:['Sgt. AL Powell']}]->(DieHard:Movie {title:'Die Hard', released:1988, tagline:'On a good day he is a great cop'})"""
# 	q_14="""CREATE (John:Person {name:'John McTiernan', born:1951})-[:DIRECTED]->(DieHard:Movie {title:'Die Hard', released:1988, tagline:'On a good day he is a great cop'})"""
# 	q_15="""CREATE (JoelS:Person {name:'Joel Silver', born:1952})-[:PRODUCED]->(DieHard:Movie {title:'Die Hard', released:1988, tagline:'On a good day he is a great cop'})"""
# 	q_16="""CREATE (Lawrence:Person {name:'Lawrence Gordon', born:1936})-[:PRODUCED]->(DieHard:Movie {title:'Die Hard', released:1988, tagline:'On a good day he is a great cop'})"""

# 	'''
# 		For inserting the data into the movie table I have created a list of queries which will attach few details about the cast/director/producer
# 		to the movie.
# 	'''
# 	list_q=[q1,q_10,q_11,q_12,q_13,q_14,q_15,q_16]

# 	'''
# 	Retrieving some of the movies pertaining to a certain actor

# 	'''

# 	c_q1='''
# 	MATCH (movie:Movie) where{name:"Tom Hanks"}) RETURN movie.title LIMIT 5
# 	'''

# 	c_q2='''
# 	MATCH (nineties:Movie) WHERE nineties.released >= 1990 AND nineties.released < 2000 RETURN nineties.title as MovieTitle,nineties.released as Released
# 	'''
# 	c_q3='''
# 	MATCH (bruce:Person {name: "Bruce Willis"})-[:ACTED_IN]->(bruceMovies) RETURN bruce,bruceMovies
# 	'''

# 	'''
# 	Delete all nodes and relationships from the graph database
# 	and to check if all nodes are disconnected or not


# 	'''
# 	delete_query=''' MATCH (n) DETACH DELETE n'''
# 	check_query=''' Match (n) return n '''

# 	lq=[]




# 	print("Session is beginning")
	
		
# 	for query in list_q:
# 		try:
#   			session.execute_write(lambda tx: tx.run(query))
# 		except:
#   			print("Error in uploading a new information")
		
		
# 	results = driver.run(c_q3).data()
# 	df_movies=pd.DataFrame()
	
# 	for record in results:
# 		print("Movie Title {} ,--> Release Date: {}".format(record['bruceMovies']['title'],record['bruceMovies']['released']))

	
# 	movieresults = driver.run(c_q2).data()
# 	list_title=[]
# 	list_released=[]
# 	for r in movieresults:
# 		list_title.append(str(r['MovieTitle']))
# 		list_released.append(int(r['Released']))
		
# 	df_movies['Title']=list_title
# 	df_movies['ReleaseYear']=list_released	
# 	print("Movie Title that release between 1990 and 2000")
# 	print("*"*50)
# 	print(df_movies)
# 	print("*"*50)

# 	"""
# 	Delete Operation
# 	"""
# 	try:
# 		driver.run(delete_query).data()
# 		# session.execute_write(lambda tx: tx.run(delete_query))
# 	except:
# 		print("Delete operation was not successfull")
# 	finally:
# 		check_r=driver.run(check_query).data()
# 		if len(check_r)==0:
# 			print("Delete operation is done!!")










# if __name__ == "__main__":
# 	time.sleep(10)
# 	function()
	



