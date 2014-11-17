__author__ = 'Marnee Dearman'
from py2neo import Node, Graph, Path, Relationship
import uuid
import collections
#from py2neo import neo4j
from agora_types import AgoraRelationship, AgoraLabel


class AgoraUser(object):
    def __init__(self, graph_db=None):
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
        self.graph_db = Graph("http://localhost:7474/db/data/")

    def get_user(self):
        user_node = self.graph_db.find_one(AgoraLabel.USER,
                                           property_key='email',
                                           property_value=self.email)
        if not user_node is None:
            self.name = user_node["name"]
            self.unique_id = user_node["unique_id"]
            self.mission_statement = user_node["mission_statement"]
            self.email = user_node["email"]
            self.is_mentor = user_node["is_mentor"]
            self.is_tutor = user_node["is_tutor"]
            self.is_visible = user_node["is_visible"]
            self.is_available_for_in_person = user_node["is_available_for_in_person"]
            self.is_admin = user_node["is_admin"]

    def create_user(self):
        """
        create a new user based on the attributes
        :return: node
        """
        unique_id = str(uuid.uuid4())
        new_user_properties = {
            "name": self.name,
            "mission_statement": self.mission_statement,
            "unique_id": unique_id,
            "email": self.email.lower(),
            "is_mentor": True,
            "is_tutor": True,
            "is_visible": True,
            "is_available_for_in_person": True,
            "is_admin": True}
        new_user_node = Node.cast(AgoraLabel.USER, new_user_properties)
        try:
            self.graph_db.create(new_user_node)
        except:
            pass
        return new_user_node

    @property
    def user_node(self):
        """
        get a user neo4j.Node
        :return: neo4j.Node
        """
        return self.graph_db.find_one(AgoraLabel.USER,
                                      property_key='email',
                                      property_value=self.email)
        # return self.graph_db.get_or_create_indexed_node(index_name=AgoraLabel.USER,
        #                                                      key='email', value=self.email)

    @property
    def user_interests(self):
        """ get user interests
        :return: list of interests
        """
        user_interests = self.graph_db.match(start_node=self.user_node,
                                             rel_type=AgoraRelationship.INTERESTED_IN,
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

    @property
    def user_groups(self):
        """

        :return: list of tuples of the groups
        """
        user_groups = self.graph_db.match(start_node=self.user_node, rel_type=AgoraRelationship.STUDIES_WITH,
                                             end_node=None)
        #create a list of tuples of interests and the users's relationship to them
        groups_list = []
        for item in user_groups:
            groups_list.append((item.end_node["name"], item["unique_id"]))
        # return [item.end_node["name"] for item in user_interests]
        return groups_list

    @property
    def user_orgs(self):
        """

        :return:
        """
        user_orgs = self.graph_db.match(start_node=self.user_node,
                                        rel_type=AgoraRelationship.MEMBER_OF,
                                        end_node=None)
        orgs_list = []
        for item in user_orgs:
            orgs_list.append(item.end_node["name"])
        return orgs_list

    def add_interest(self, interest_node):
        """ Add interest to user
        :param interest_node:py2neo Node
        :return: List of interests
        """
        user_interest_relationship = Relationship(start_node=self.user_node,
                                                  rel=AgoraRelationship.INTERESTED_IN,
                                                  end_node=interest_node)
        self.graph_db.create_unique(user_interest_relationship)
        return self.user_interests

    def update_user(self):
        pass

    def make_admin(self):
        #new_user = self.graph_db.get_or_create_indexed_node(index_name=AgoraLabel.USER, key='email', value=self.email)
        self.user_node.add_labels(AgoraLabel.ADMIN)

    def add_goal(self, goal_node, goal_relationship_properties=None):
        """
        Add goal to user
        :param goal_node: py2neo Node
        :return: List of user goals
        """
        #get user node with unique id
        # user_node = self.graph_db.get_or_create_indexed_node(index_name=AgoraLabel.USER,
        #                                                      key='email', value=self.email)
        #create relationship between user and interest node
        user_goal_relationship = Relationship(start_node=self.user_node,
                                              rel=AgoraRelationship.HAS_GOAL,
                                              end_node=goal_node)

        self.graph_db.create_unique(user_goal_relationship)
        #TODO set properties on the relationship -- may use a unique id as the key
        return self.user_goals

    def add_group(self, group_node, group_relationship_properties=None):
        """
        Add user as member of group
        :param group_node: py2neo Node
        :return:
        """

        user_group_relationship = Relationship(start_node=self.user_node,
                                               rel=AgoraRelationship.MEMBER_OF,
                                               end_node=group_node)
        self.graph_db.create_unique(user_group_relationship)
        #TODO set properties on the relationsip
        # group_relationship_properties["unique_id"] = str(uuid.uuid4())

    def add_organization(self, org_node):
        """
        add user to organization
        :param org_node: py2neo Node
        :return: list of tuple of interests
        """
        user_org_relationship = Relationship(start_node=self.user_node,
                                             rel=AgoraRelationship.MEMBER_OF,
                                             end_node=org_node)
        self.graph_db.create_unique(user_org_relationship)
