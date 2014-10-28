__author__ = 'Marnee Dearman'
from agora_db.py2neo_user import AgoraUser
from agora_db.py2neo_interest import AgoraInterest
import py2neo
from py2neo import neo4j

graph_db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")

agora_user = AgoraUser(graph_db)
agora_user.email = "ralphie@email.com"
agora_user.get_user()
print agora_user.name

