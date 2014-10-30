__author__ = 'Marnee Dearman'
from agora_db.py2neo_user import AgoraUser
from agora_db.py2neo_interest import AgoraInterest
import py2neo
from py2neo import neo4j

graph_db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")

#get or create a new user with an index


#get a new user by email address
agora_user = AgoraUser(graph_db)
agora_user.email = "ralphie@email.com"
agora_user.get_user()
print agora_user.name
new_user = agora_user.create_user()
print new_user["name"]
