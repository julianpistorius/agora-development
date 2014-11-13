__author__ = 'Marnee Dearman'
import py2neo
import uuid
import collections
from py2neo import neo4j
from agora_types import AgoraRelationship, AgoraLabel

class AgoraAchievement(object):
    def __init__(self, graph_db):
        self.name = None
        self.unique_id = None
        self.description = None
        self.title = None
        self.is_visible = True
        self.date = None