__author__ = 'Marnee Dearman'
from agora_db.py2neo_user import AgoraUser
from agora_db.py2neo_interest import AgoraInterest
from agora_db.py2neo_goal import AgoraGoal
from agora_db.py2neo_group import AgoraGroup
from agora_db.py2neo_organization import AgoraOrganization
from agora_db.agora_types import AgoraRelationship, AgoraLabel
import py2neo
from py2neo import neo4j
import datetime

import time

graph_db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")
#start over seeding the database
graph_db.clear()

#create admins USER Marnee

admin_user = AgoraUser(graph_db)
admin_user.name = "Marnee"
admin_user.mission_statement = "Developing the Agora"
admin_user.email = "marnee@agorasociety.com"
admin_user.is_mentor = True
admin_user.is_tutor = True
admin_user.is_visible = True
admin_user.is_available_for_in_person = True
admin_user.is_admin = True
admin_user.get_user()
print admin_user.unique_id
if admin_user.unique_id is None:
    admin_user.create_user()
print admin_user


#create new users for the THURSDAY DEMO DAY group
#JULIAN PISTORIUS
print 'make julian'
user = AgoraUser(graph_db)
user.name = "Julian"
user.mission_statement = "Learn all the things."
user.email = "julian@comanage.com"
user.is_mentor = True
user.is_tutor = True
user.is_visible = True
user.is_available_for_in_person = True
user.is_admin = True
user.get_user()
print user.unique_id
if user.unique_id is None:
    user.create_user()
# user.add_interest(interest_id=startup_id,
#                   interest_description='')
#
#
# #DAN
print 'make dan'
user = AgoraUser(graph_db)
user.name = "Dan"
user.mission_statement = "Learn all the things."
user.email = "dan@comanage.com"
user.is_mentor = True
user.is_tutor = True
user.is_visible = True
user.is_available_for_in_person = True
user.is_admin = True
user.get_user()
print user.unique_id
if user.unique_id is None:
    user.create_user()
user.add_interest(interest_id=startup_id,
                  interest_description='')
# print admin_user
#
# #FRANK
print 'make frank'
user = AgoraUser(graph_db)
user.name = "Frank"
user.mission_statement = "Learn all the things."
user.email = "frank@comanage.com"
user.is_mentor = True
user.is_tutor = True
user.is_visible = True
user.is_available_for_in_person = True
user.is_admin = True
user.get_user()
print user.unique_id
if user.unique_id is None:
    user.create_user()
user.add_interest(interest_id=startup_id,
                  interest_description='')
# print admin_user

