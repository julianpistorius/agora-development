__author__ = 'Marnee Dearman'
import py2neo
import uuid
import collections
from py2neo import neo4j
from agora_types import AgoraRelationship, AgoraLabel

class AgoraGroup(object):
    def __init__(self, graph_db):
        self.name = None
        self.unique_id = None
        self.description = None
        self.is_open = None
        self.is_invite_only = None
        self.meeting_location = None
        self.next_meeting_date = None
        self.members = []
        self.interests = []
        self.graph_db = graph_db

    def create_group(self):
        pass

    def update_group(self):
        pass

    def close_group(self):
        pass



