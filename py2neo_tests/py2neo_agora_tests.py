__author__ = 'Marnee Dearman'
from agora_db.py2neo_user import AgoraUser
from agora_db.py2neo_interest import AgoraInterest
import py2neo
from py2neo import neo4j

import time

graph_db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")

agora_user = AgoraUser(graph_db)

# agora_user.name = "Marnee"
# print "Marnee user", agora_user.user_interests

#create new user
# new_user = AgoraUser()
# new_user.name = "Ralphie"
# new_user.email = "ralphie@email.com"
# new_user.description = "I'm interested in the art of motorcycle maintenance, and learning all kinds of other things."
# created_user = new_user.create_user()
# print created_user

#create new interest
# new_interest = AgoraInterest(graph_db)
# new_interest.name = "Python"
# new_interest.description = "Learning the python programming language."
# created_interest = new_interest.create_interest()
# print created_interest

#get interest
# get_interest = AgoraInterest(graph_db)
# get_interest.name = "TEST"
# get_interest.description = "DESCRIPTION"
# found_interest = get_interest.get_interest()
# print 'found interest', found_interest

#add interest to user
# agora_user = AgoraUser(graph_db)
# agora_user.unique_id = "7e0570a4-15db-4b45-8085-88135334876e"
# print "user interests", agora_user.user_interests
#
# agora_user.add_interest("cb1ae529-e674-4413-9244-df3b67c4e871", "Just starting out and need help learning the python basics.")
# user_interests = agora_user.user_interests
# print 'user interests with added', user_interests




