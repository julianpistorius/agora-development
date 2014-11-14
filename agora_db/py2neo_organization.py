__author__ = 'Marnee Dearman'
import py2neo
import uuid
import collections
from py2neo import neo4j
from agora_types import AgoraRelationship, AgoraLabel

class AgoraOrganization(object):
    def __init__(self):
        self.name = None
        self.unique_id = None
        self.mission_statement = None
        self.email = None
        self.is_open = False
        self.website = None
        self.graph_db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")

    def create_organization(self):
        """
        create a new organization
        :return:
        """
        self.unique_id = str(uuid.uuid4())
        new_org_properties = {
            "name": self.name,
            "mission_statement": self.mission_statement,
            "unique_id": self.unique_id,
            "email": self.email,
            "is_open": self.is_open,
            "website": self.website}
        new_org = self.graph_db.get_or_create_indexed_node(index_name=AgoraLabel.ORGANIZATION,
                                                           key='name', value=self.name,
                                                           properties=new_org_properties)
        new_org.add_labels(AgoraLabel.ORGANIZATION)
        return new_org