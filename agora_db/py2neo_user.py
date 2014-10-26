__author__ = 'Marnee Dearman'
import py2neo
import uuid
import collections
from py2neo import neo4j
from agora_types import AgoraRelationship, AgoraLabels


class AgoraUser(object):
    def __init__(self):
        self.name = None
        self.unique_id = None
        self.description = None
        self.email = None
        self.is_mentor = False
        self.is_tutor = False
        self.is_visible = True
        self.is_available_for_in_person = True
        # self._interests_list = None
        self.is_admin = False
        self.graph_db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")

    def create_user(self):
        """
        create a new user based on the attributes
        :return: node
        """
        self.unique_id = str(uuid.uuid4())
        new_user_properties = {
            "name": self.name,
            "unique_id": self.unique_id,
            "email": self.email,
            "is_mentor": self.is_mentor,
            "is_tutor": self.is_tutor,
            "is_visible": self.is_visible,
            "is_available_for_in_person": self.is_available_for_in_person,
            "is_admin": self.is_admin}
        new_user = neo4j.Node.abstract(
            name=self.name,
            unique_id=self.unique_id,
            email=self.email,
            is_mentor=self.is_mentor,
            is_tutor=self.is_tutor,
            is_visible=self.is_visible,
            is_available_for_in_person=self.is_available_for_in_person,
            is_admin=self.is_admin
        )
        new_user, = self.graph_db.create(new_user)
        new_user.add_labels(AgoraLabels.User)
        return new_user

    @property
    def user_interests(self):
        """ get user interests
        :return: list of interests
        """
        user_nodes = self.graph_db.find(AgoraLabels.User, "unique_id", self.unique_id)
        user_node = user_nodes.next()
        user_interests = self.graph_db.match(start_node=user_node, rel_type=AgoraRelationship.INTERESTED_IN,
                                             end_node=None)
        #create a list of tuples of interests and the users's relationship to them
        interests_list = []
        for item in user_interests:
            interests_list.append((item.end_node["name"], item["description"]))
        # return [item.end_node["name"] for item in user_interests]
        return interests_list

    def add_interest(self, interest_id, interest_description):
        """ Add interest to user
        :param interest:
        :return: none
        """
        # check that interest_description is a dictionary?

        #get user node with unique id
        user_nodes = self.graph_db.find(AgoraLabels.User, "unique_id", self.unique_id)
        user_node = user_nodes.next()

        #get interest node with interest_id (interest unique_id)
        interest_nodes = self.graph_db.find(AgoraLabels.INTEREST, "unique_id", interest_id)
        interest_node = interest_nodes.next()

        #create relationship between user and interest node
        neo4j.Path(user_node, AgoraRelationship.INTERESTED_IN, interest_node).get_or_create(graph_db=self.graph_db)

        #get INTERESTED_IN relationship between user and interest -- set the relationship description
        user_interests = self.graph_db.match(start_node=user_node, rel_type=AgoraRelationship.INTERESTED_IN,
                                             end_node=interest_node)
        new_interest_node = user_interests.next()
        new_interest_node.set_properties({'description': interest_description})
        #print new_interest_node






