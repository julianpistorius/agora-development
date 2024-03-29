__author__ = 'Marnee Dearman'
from py2neo import Node, Graph, Relationship
import uuid
import collections
#from py2neo import neo4j
from agora_db.agora_types import AgoraRelationship, AgoraLabel
from agora_db.py2neo_user import AgoraUser
from agora_db.py2neo_interest import AgoraInterest
graph_db = Graph()
unique_id = str(uuid.uuid4())
new_user_properties = {
    "name": "Marnee",
    "mission_statement": "Develop the Agora",
    "unique_id": unique_id,
    "email": 'marnee@agorasociety.com'.lower(),
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
                                      property_value="marnee@agorasociety.com".lower())
print user_node["email"]

user = AgoraUser()
user.email = "marnee@agorasociety.com"
print user.user_interests

interest = AgoraInterest()
interest.name = 'SAMPLE'
interest.description = 'SAMPLE DESCRIPTION'
new_interest_node = interest.create_interest()

user_interest_relationship_node = Relationship(start_node=user_node,
                                               rel=AgoraRelationship.INTERESTED_IN,
                                               end_node=new_interest_node)
try:
    graph_db.create_unique(user_interest_relationship_node)
except:
    print 'relationship already exists'
