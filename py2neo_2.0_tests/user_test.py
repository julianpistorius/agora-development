__author__ = 'Marnee Dearman'
from py2neo import Node, Graph
import uuid
import collections
#from py2neo import neo4j
from agora_db.agora_types import AgoraRelationship, AgoraLabel
graph_db = Graph()
unique_id = str(uuid.uuid4())
new_user_properties = {
    "name": "Marnee",
    "mission_statement": "Develop the Agora",
    "unique_id": unique_id,
    "email": 'marnee@agorasociety.com',
    "is_mentor": True,
    "is_tutor": True,
    "is_visible": True,
    "is_available_for_in_person": True,
    "is_admin": True}
new_user_node = Node.cast(AgoraLabel.USER, new_user_properties)
try:
    graph_db.create(new_user_node)
except:
    print 'Node found'

user_node = graph_db.find_one(AgoraLabel.USER,
                                      property_key='email',
                                      property_value="marnee@agorasociety.com")
print user_node["email"]