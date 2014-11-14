__author__ = 'Marnee Dearman'
import py2neo
import uuid
import collections
from py2neo import neo4j
from agora_types import AgoraRelationship, AgoraLabel


class AgoraUser(object):
    def __init__(self, graph_db):
        self.name = None
        self.unique_id = None
        self.mission_statement = None
        self.email = None
        self.is_mentor = False
        self.is_tutor = False
        self.is_visible = True
        self.is_available_for_in_person = True
        # self._interests_list = None
        self.is_admin = False
        self.graph_db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")

    def get_user(self):
        user_nodes = self.graph_db.find(AgoraLabel.USER, "email", self.email)
        try:
            user_node = user_nodes.next()
            self.name = user_node["name"]
            self.unique_id = user_node["unique_id"]
            self.mission_statement = user_node["mission_statement"]
            self.email = user_node["email"]
            self.is_mentor = user_node["is_mentor"]
            self.is_tutor = user_node["is_tutor"]
            self.is_visible = user_node["is_visible"]
            self.is_available_for_in_person = user_node["is_available_for_in_person"]
            self.is_admin = user_node["is_admin"]
        except:
            pass

    def create_user(self):
        """
        create a new user based on the attributes
        :return: node
        """
        self.unique_id = str(uuid.uuid4())
        new_user_properties = {
            "name": self.name,
            "mission_statement": self.mission_statement,
            "unique_id": self.unique_id,
            "email": self.email,
            "is_mentor": self.is_mentor,
            "is_tutor": self.is_tutor,
            "is_visible": self.is_visible,
            "is_available_for_in_person": self.is_available_for_in_person,
            "is_admin": self.is_admin}
        new_user = self.graph_db.get_or_create_indexed_node(index_name=AgoraLabel.USER,
                                                            key='email', value=self.email,
                                                            properties=new_user_properties)
        new_user.add_labels(AgoraLabel.USER)
        return new_user

    @property
    def user_node(self):
        """
        get a user neo4j.Node
        :return: neo4j.Node
        """
        return self.graph_db.get_or_create_indexed_node(index_name=AgoraLabel.USER,
                                                             key='email', value=self.email)

    @property
    def user_interests(self):
        """ get user interests
        :return: list of interests
        """
        user_interests = self.graph_db.match(start_node=self.user_node, rel_type=AgoraRelationship.INTERESTED_IN,
                                             end_node=None)
        #create a list of tuples of interests and the users's relationship to them
        interests_list = []
        for item in user_interests:
            interests_list.append((item.end_node["name"], item["description"]))
        # return [item.end_node["name"] for item in user_interests]
        return interests_list

    @property
    def user_goals(self):
        """ get user interests
        :return: list of interests
        """
        user_goals = self.graph_db.match(start_node=self.user_node, rel_type=AgoraRelationship.HAS_GOAL,
                                             end_node=None)
        #create a list of tuples of interests and the users's relationship to them
        goals_list = []
        for item in user_goals:
            goals_list.append((item.end_node["title"], item["description"]))
        # return [item.end_node["name"] for item in user_interests]
        return goals_list

    def add_interest(self, interest_id, interest_relationship_properties):
        """ Add interest to user
        :param interest:
        :return: none
        """
        # check that interest_description is a dictionary?

        #get interest node with interest_id (interest unique_id)
        interest_node = self.graph_db.get_indexed_node(index_name=AgoraLabel.INTEREST,
                                                       key='unique_id', value=interest_id)
        #create relationship between user and interest node
        neo4j.Path(self.user_node,
                   AgoraRelationship.INTERESTED_IN,
                   interest_node).get_or_create(graph_db=self.graph_db)

        #get INTERESTED_IN relationship between user and interest -- set the relationship description
        user_interest_relationship = self.graph_db.match(start_node=self.user_node, rel_type=AgoraRelationship.INTERESTED_IN,
                                             end_node=interest_node)
        new_interest_node = user_interest_relationship.next()
        interest_relationship_properties["unique_id"] = str(uuid.uuid4())
        new_interest_node.set_properties(interest_relationship_properties)
        #print new_interest_node

    def update_user(self):
        pass

    def make_admin(self):
        #new_user = self.graph_db.get_or_create_indexed_node(index_name=AgoraLabel.USER, key='email', value=self.email)
        self.user_node.add_labels(AgoraLabel.ADMIN)

    def add_goal(self, goal_node, goal_relationship_properties=None):
        """
        Add goal to user
        :param goal_node:
        :return:
        """
        #get user node with unique id
        # user_node = self.graph_db.get_or_create_indexed_node(index_name=AgoraLabel.USER,
        #                                                      key='email', value=self.email)
        #create relationship between user and interest node
        neo4j.Path(self.user_node,
                   AgoraRelationship.HAS_GOAL,
                   goal_node).get_or_create(graph_db=self.graph_db)
        #TODO set properties on the relationship -- may use a unique id as the key
        goal_relationship_properties["unique_id"] = str(uuid.uuid4())

    def add_group(self, group_node, group_relationship_properties=None):
        """
        Add user as member of group
        :param group_node:
        :return:
        """
        neo4j.Path(self.user_node,
                   AgoraRelationship.MEMBER_OF,
                   group_node).get_or_create(graph_db=self.graph_db)
        #TODO set properties on the relationsip
        group_relationship_properties["unique_id"] = str(uuid.uuid4())