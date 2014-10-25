__author__ = 'Marnee Dearman'
import py2neo
import uuid
from py2neo import neo4j
from agora_types import AgoraRelationship, AgoraLabels

class AgoraUser(object):
    def __init__(self):
        self.name = None
        self.unique_id = None
        self.description = None
        self.email = None
        self.is_mentor = None
        self.is_tutor = None
        self.is_visible = None
        self.is_available_for_in_person = None
        #self._interests_list = None
        self.is_admin = None
        self.graph_db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")

    def create_user(self):
        """
        create a new user based on the attributes
        :return: node
        """
        self.unique_id = uuid.uuid4()
        new_user_properties = {
            "name": self.name,
            "unique_id": self.unique_id,
            "email": self.email,
            "is_mentor": self.is_mentor,
            "is_tutor": self.is_tutor,
            "is_visible": self.is_visible}
        new_user = neo4j.Node.abstract(new_user_properties)
        new_user, = self.graph_db.create(new_user)
        new_user.add_labels(AgoraLabels.User)

    @property
    def user_interests(self):
        """ get user interests
        :return: list of interests
        """
        user_nodes = self.graph_db.find(AgoraLabels.User, "name", self.name)
        user_node = user_nodes.next()
        user_interests = self.graph_db.match(start_node=user_node, rel_type=AgoraRelationship.INTERESTED_IN, end_node=None)
        return [item.end_node["name"] for item in user_interests]

    def add_interest(self, interest, interest_description):
        """ Add interest to user
        :param interest:
        :return: none
        """
        #check that interest_description is a dictionary?

        user_nodes = self.graph_db.find(AgoraLabels.User, "name", self.name)
        user_node = user_nodes.next()

        interest_nodes = self.find(AgoraLabels.INTEREST, "name", interest)
        interest_node = interest_nodes.next()

        new_relationship = neo4j.Path(user_node, AgoraRelationship.INTERESTED_IN, interest_node).get_or_create(graph_db=self.graph_db)
        new_relationship.set_properties(interest_description)
    #dlfkgjdslgkjdfgkfdg

    #dlkdfgf;dsghfd;gkh





