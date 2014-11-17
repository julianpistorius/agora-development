__author__ = 'Marnee Dearman'
import py2neo
import uuid
import collections
from py2neo import Graph, Node, Relationship
from agora_types import AgoraRelationship, AgoraLabel

class AgoraGoal(object):
    def __init__(self, graph_db):
        self.title = None
        self.unique_id = None
        self.description = None
        self.start_date = None
        self.end_date = None
        self.interests = []
        self.achievements = []
        self.graph_db = Graph()

    @property
    def goal_node(self):
        """
        get a single goal node based on the attributes of the goal
        :return: neo4j.Node
        """
        goal_node = self.graph_db.find_one(AgoraLabel.GOAL,
                                           property_key='unique_id',
                                           property_value=self.unique_id)
        return goal_node

    @property
    def goal_interests(self):
        goal_interests = self.graph_db.match(start_node=self.goal_node,
                                             rel_type=AgoraRelationship.GOAL_INTEREST,
                                             end_node=None)
        goal_interests_list = []
        for item in goal_interests:
            goal_interests_list.append((item["name"], item["description"]))

        return goal_interests_list

    def create_goal(self):
        """
        create a goal and relate to user
        :return: neo4j.Node
        """
        # goal_node = self.get_goal() #TO GO get goal to prevent duplication?  maybe not needed -- MMMD 11/12/2014
        # if goal_node is None:
        self.unique_id = str(uuid.uuid4())
        new_goal_properties = {
            "title": self.title,
            "description": self.description,
            "unique_id": self.unique_id,
            "start_date": self.start_date,
            "end_date": self.end_date}
        new_goal = Node.cast(AgoraLabel.GOAL, new_goal_properties)
        return new_goal

    def update_goal(self):
        """
        update goal related to user
        :return:
        """
        pass

    def link_goal_to_achievement(self):
        pass

    def add_interest(self, interest_node):
        goal_interest_relationship = Relationship(start_node=self.goal_node,
                                                  rel=AgoraRelationship.GOAL_INTEREST,
                                                  end_node=interest_node)
        self.graph_db.create_unique(goal_interest_relationship)
        return

    def get_goal(self):
        pass

    def delete_goal(self):
        pass



