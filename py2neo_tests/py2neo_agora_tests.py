__author__ = 'Marnee Dearman'
from agora_db.py2neo_user import AgoraUser
from agora_db.py2neo_interest import AgoraInterest

import time

agora_user = AgoraUser()

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
# new_interest = AgoraInterest()
# new_interest.name = "Python"
# new_interest.description = "Learning the python programming language."
# created_interest = new_interest.create_interest()
# print created_interest

#add interest to user
agora_user = AgoraUser()
agora_user.unique_id = "7e0570a4-15db-4b45-8085-88135334876e"
print "user interests", agora_user.user_interests

agora_user.add_interest("cb1ae529-e674-4413-9244-df3b67c4e871", "Just starting out and need help learning the python basics.")
user_interests = agora_user.user_interests
# print 'user interests added', user_interests, user_interests.description


