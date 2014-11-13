__author__ = 'Marnee Dearman'
import py2neo
import uuid
import collections
from py2neo import neo4j
from agora_types import AgoraRelationship, AgoraLabel

class AgoraInterest(object):
    def __init__(self, graph_db):
        self.name = None
        self.unique_id = None
        self.description = None
        self.graph_db = graph_db
        #neo4j.GraphDatabaseService("http://localhost:7474/db/data/")

    def create_interest(self):
        """
        create an interest node based on the class attributes
        :return: node
        """
        #TO DO -- create as indexed node?
        self.unique_id = str(uuid.uuid4())
        new_interest_properties = {
            "name": self.name,
            "description": self.description,
            "unique_id": self.unique_id
        }
        new_interest = self.graph_db.get_or_create_indexed_node(index_name=AgoraLabel.INTEREST,
                                                            key='unique_id', value=self.unique_id,
                                                            properties=new_interest_properties)
        new_interest.add_labels(AgoraLabel.INTEREST)
        return new_interest

        # interest_node = self.get_interest()
        # if interest_node is None:
        #     self.unique_id = str(uuid.uuid4())
        #     new_interest = neo4j.Node.abstract(name=self.name, desciption=self.description, unique_id=self.unique_id)
        #     created_interest, = self.graph_db.create(new_interest)
        #     created_interest.add_labels(AgoraLabel.INTEREST)
        #     return created_interest
        # else:
        #     return interest_node

    def get_interest(self):
        """
        get interest node
        :return:
        """
        interest_nodes = self.graph_db.find(AgoraLabel.INTEREST, "name", self.name)
        try:
            interest_node = interest_nodes.next()
            self.name = interest_node["name"]
            self.unique_id = interest_node["unique_id"]
            self.description = interest_node["description"]
            return interest_node
        except:
            print 'not found'
            return None
