__author__ = 'Marnee Dearman'
import py2neo
from py2neo import neo4j
from agora_types import AgoraRelationship, AgoraLabels

class AgoraGroup(object):
    def __init__(self):
        self.name = None
        self.unique_id = None
        self.description = None
        self.is_open = None
        self.is_invite_only = None
        self.meeting_location = None
        self.next_meeting_date = None
        self.graph_db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")

