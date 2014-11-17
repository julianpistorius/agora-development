__author__ = 'Marnee Dearman'
import uuid

from py2neo import Graph, Node

# from py2neo import neo4j
from agora_types import AgoraLabel


class AgoraInterest(object):
    def __init__(self, graph_db=None):
        self.name = None
        self.unique_id = None
        self.description = None
        self.graph_db = Graph()
        #neo4j.GraphDatabaseService("http://localhost:7474/db/data/")

    @property
    def interest_node(self):
        return self.graph_db.find_one(AgoraLabel.INTEREST,
                                      property_key='unique_id',
                                      property_value=self.unique_id)

    def create_interest(self):
        """
        create an interest node based on the class attributes
        :return: py2neo Node
        """
        #TODO -- create as indexed node?
        self.unique_id = str(uuid.uuid4())
        new_interest_properties = {
            "name": self.name,
            "description": self.description,
            "unique_id": self.unique_id
        }

        new_interest_node = Node.cast(AgoraLabel.INTEREST, new_interest_properties)
        try:
            self.graph_db.create(new_interest_node)
        except:
            pass

        return new_interest_node

        # interest_node = self.get_interest()
        # if interest_node is None:
        #     self.unique_id = str(uuid.uuid4())
        #     new_interest = neo4j.Node.abstract(name=self.name, desciption=self.description, unique_id=self.unique_id)
        #     created_interest, = self.graph_db.create(new_interest)
        #     created_interest.add_labels(AgoraLabel.INTEREST)
        #     return created_interest
        # else:
        #     return interest_node

    def get_interest_by_name(self):
        """
        get interest node
        :return:
        """
        interest_node = self.graph_db.find_one(AgoraLabel.INTEREST,
                                               property_key='name',
                                               property_value=self.name)

        if not interest_node is None:
            self.name = interest_node["name"]
            self.unique_id = interest_node["unique_id"]
            self.description = interest_node["description"]
        return interest_node

    def get_interest_by_unique_id(self):
        """
        get interest node by unique id
        sets attributes of this interest instance to properties on node found
        :return: noe4j.Node
        """
        interest_node = self.graph_db.find_one(AgoraLabel.INTEREST,
                                               property_key='unique_id',
                                               property_value=self.unique_id)
        if not interest_node is None:
            self.name = interest_node["name"]
            self.unique_id = interest_node["unique_id"]
            self.description = interest_node["description"]

        return interest_node