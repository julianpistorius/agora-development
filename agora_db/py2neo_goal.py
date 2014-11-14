__author__ = 'Marnee Dearman'
import py2neo
import uuid
import collections
from py2neo import neo4j
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
        self.graph_db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")

    @property
    def goal_node(self):
        """
        get a single goal node based on the attributes of the goal
        :return: neo4j.Node
        """
        goal_node = self.graph_db.get_or_create_indexed_node(AgoraLabel.GOAL,
                                                             key='unique_id',
                                                             value=self.unique_id)
        return goal_node

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

        new_goal = self.graph_db.get_or_create_indexed_node(index_name=AgoraLabel.GOAL, key='unique_id',
                                                            value=self.unique_id,
                                                            properties=new_goal_properties)
        new_goal.add_labels(AgoraLabel.GOAL)
        return new_goal

        #
        # new_goal = neo4j.Node.abstract(name=self.title, desciption=self.description, unique_id=self.unique_id)
        # created_goal, = self.graph_db.create(new_goal)
        # created_goal.add_labels(AgoraLabel.GOAL)
        # #self.add_goal(created_goal)
        # return created_goal
        # else:
        #     return goal_node

    def update_goal(self):
        """
        update goal related to user
        :return:
        """
        pass

    def link_goal_to_achievement(self):
        pass

    def link_goal_to_interests(self, goal_node, interests_unique_id_list):
        for interest_unique_id in interests_unique_id_list:
            #GET interest node with interest_id (interest unique_id)
            interest_node = self.graph_db.get_or_create_indexed_node(index_name=AgoraLabel.INTEREST,
                                                                      key='unique_id',
                                                                      value=interest_unique_id)

            #CREATE relationship between goal and interest node
            neo4j.Path(goal_node,
                       AgoraRelationship.GOAL_INTEREST,
                       interest_node).get_or_create(graph_db=self.graph_db)

    def get_goal(self):
        pass

    def delete_goal(self):
        pass



