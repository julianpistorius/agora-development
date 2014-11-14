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

#create INTERESTS
# Marnee INTERESTS -- Kettlebells, Python, Agorism
user_interest = AgoraInterest(graph_db)
user_interest.name = "Kettlebells"
user_interest.description = "Building strength with those cannonballs with handles."
user_interest.get_interest()
print "unique id", user_interest.unique_id
if user_interest.unique_id is None:
    user_interest.create_interest()
print user_interest.unique_id

user_interest = AgoraInterest(graph_db)
user_interest.name = "Python"
user_interest.description = "Building code with that funny dynamic typing language."
user_interest.get_interest()
print user_interest.unique_id
if user_interest.unique_id is None:
    user_interest.create_interest()
print user_interest.unique_id

user_interest = AgoraInterest(graph_db)
user_interest.name = "Agorism"
user_interest.description = "Peaceful revolution."
user_interest.get_interest()
print user_interest.unique_id
if user_interest.unique_id is None:
    user_interest.create_interest()
print user_interest.unique_id

user_interest = AgoraInterest(graph_db)
user_interest.name = "Internet Startup"
user_interest.description = "Innovation and disruption."
user_interest.get_interest()
print user_interest.unique_id
if user_interest.unique_id is None:
    user_interest.create_interest()
print user_interest.unique_id

#going to use this to link up some users to the startup interest
startup_id = user_interest.unique_id

#END create INTERESTS

# #create RELATIONSHIPS with Marnee
user = AgoraUser(graph_db)
user.email = "marnee@agorasociety.com"
user.get_user()
interest = AgoraInterest(graph_db)
interest.name = "Kettlebells"
interest.get_interest()
if not interest.unique_id is None:
    user.add_interest(interest.unique_id, "Trying to get stronger with kettlebells.")
print user.user_interests
#
user = AgoraUser(graph_db)
user.email = "marnee@agorasociety.com"
user.get_user()
interest = AgoraInterest(graph_db)
interest.name = "Agorism"
interest.get_interest()
if not interest.unique_id is None:
    user.add_interest(interest.unique_id, "Peaceful revolutionary.")
print user.user_interests
#
user = AgoraUser(graph_db)
user.email = "marnee@agorasociety.com"
user.get_user()
interest = AgoraInterest(graph_db)
interest.name = "Python"
interest.get_interest()
if not interest.unique_id is None:
    user.add_interest(interest.unique_id, "Building the Agora on Python")
print user.user_interests

user = AgoraUser(graph_db)
user.email = "marnee@agorasociety.com"
user.get_user()
interest = AgoraInterest(graph_db)
interest.name = "Internet Startup"
interest.get_interest()
if not interest.unique_id is None:
    user.add_interest(interest.unique_id, "Starting a new internet business and software innovation.")
print user.user_interests


#create GOALS
#create GOALS for MARNEE
# user = AgoraUser(graph_db)
# user.email = "marnee@agorasociety.com"
# user.get_user()
#
# new_goal = AgoraGoal(graph_db)
# new_goal.title = "Improve kettlebell swing"
# new_goal.description = "I want to swing heavy and do it without hurting my back"
# created_goal = new_goal.create_goal()
# user.add_goal(created_goal)
#
# print user.user_goals

#create ACHIEVEMENTS

#create STUDY GROUPS
study_group = AgoraGroup(graph_db)
study_group.name = "Thursday Demo Day"
study_group.description = "Weekly meeting for Tucson internet startups.  " \
                          "We demo our projects, talk about goals, and discuss issues we may be having."
study_group.is_invite_only = True
study_group.is_open = True
study_group.meeting_location = "Soho Tucson"
study_group.next_meeting_date = datetime.datetime(year=2014, month=11, day=13, hour=18, minute=30)
study_group.group_leader_username = "dan@comanage.com"
new_study_group = study_group.create_group()

#link GROUP to INTEREST
study_group.add_interest('832e617f-c8dc-4621-966b-476342e436b2', 'Helping Tucsonans develop their startups and stay on track.' )

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
user.add_interest(interest_id=startup_id,
                  interest_description='')
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

#link USERs to GROUPS

