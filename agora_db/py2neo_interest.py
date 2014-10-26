__author__ = 'Marnee Dearman'
import py2neo
import uuid
from py2neo import neo4j, node
from agora_types import AgoraRelationship, AgoraLabels

class AgoraInterest(object):
    def __init__(self):
        self.name = None
        self.unique_id = None
        self.description = None
        self.graph_db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")

    def create_interest(self):
        """
        create an interest node based on the class attributes
        :return: node
        """
        self.unique_id = str(uuid.uuid4())
        new_interest = neo4j.Node.abstract(name=self.name, desciption=self.description, unique_id=self.unique_id)
        created_interest, = self.graph_db.create(new_interest)
        created_interest.add_labels(AgoraLabels.INTEREST)
        return created_interest

    def get_interest(self):
        pass

