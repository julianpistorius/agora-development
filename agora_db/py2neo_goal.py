__author__ = 'Marnee Dearman'
import py2neo
import uuid
import collections
from py2neo import neo4j
from agora_types import AgoraRelationship, AgoraLabels

class AgoraGoal(object):
    def __init__(self, graph_db):
        self.name = None
        self.unique_id = None
        self.description = None
        self.interests = []
        self.achievements = []
        self.graph_db = graph_db
        #neo4j.GraphDatabaseService("http://localhost:7474/db/data/")

    def create_goal(self):
        pass

    def update_goal(self):
        pass

    def link_goal_to_achievement(self):
        pass

    def delete_goal(self):
        pass

