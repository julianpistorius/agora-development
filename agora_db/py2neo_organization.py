__author__ = 'Marnee Dearman'
import uuid

from py2neo import Graph, Node

from agora_types import AgoraRelationship, AgoraLabel


class AgoraOrganization(object):
    def __init__(self):
        self.name = None
        self.unique_id = None
        self.mission_statement = None
        self.email = None
        self.is_open = False
        self.is_invite_only = False
        self.website = None
        self.graph_db = Graph()

    @property
    def org_node(self):
        return self.graph_db.find_one(AgoraLabel.ORGANIZATION,
                                      property_key='name',
                                      property_value=self.name)

    @property
    def org_members(self):
        """
        list of the members of the organization
        :return: list of tuple of member name, email
        """
        org_members_nodes = self.graph_db.match(start_node=self.org_node,
                                                rel_type=AgoraRelationship.MEMBER_OF,
                                                end_node=None)
        org_members_list = []
        for item in org_members_nodes:
            org_members_list.append((item.end_node["name"], item.end_node["email"]))
        return org_members_list

    def create_organization(self):
        """
        create a new organization
        :return: py2neo Node
        """
        self.unique_id = str(uuid.uuid4())
        new_org_properties = {
            "name": self.name,
            "mission_statement": self.mission_statement,
            "unique_id": self.unique_id,
            "email": self.email,
            "is_open": self.is_open,
            "is_invite_only": self.is_invite_only,
            "website": self.website}

        new_org_node = Node.cast(AgoraLabel.ORGANIZATION, new_org_properties)
        self.graph_db.create(new_org_node)

        return new_org_node