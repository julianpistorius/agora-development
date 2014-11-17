__author__ = 'Marnee Dearman'
import uuid

from py2neo import Graph, Node, Relationship

from agora_types import AgoraRelationship, AgoraLabel


class AgoraGroup(object):
    def __init__(self, graph_db):
        self.name = None
        self.unique_id = None
        self.description = None
        self.is_open = None
        self.is_invite_only = None
        self.meeting_location = None
        self.next_meeting_date = None
        self.members = []
        self.interests = []
        self.group_leader_username = None
        self.graph_db = Graph()

    @property
    def group_node(self):
        """
        get a group node based on the unique id attribute
        :return: neo4j.Node
        """
        return self.graph_db.find_one(AgoraLabel.STUDYGROUP,
                                      property_key='unique_id',
                                      property_value=self.unique_id)

    @property
    def group_interests(self):
        """ get user interests
        :return: list of interests
        """
        group_interests = self.graph_db.match(start_node=self.group_node,
                                              rel_type=AgoraRelationship.INTERESTED_IN,
                                              end_node=None)
        # create a list of tuples of interests and the users's relationship to them
        interests_list = []
        for item in group_interests:
            interests_list.append((item.end_node["name"], item["description"]))
        # return [item.end_node["name"] for item in user_interests]
        return interests_list

    def create_group(self):
        """
        create new study group or circle
        :return: py2neo Node
        """
        self.unique_id = str(uuid.uuid4())
        new_group_properties = {
            "name": self.name,
            "description": self.description,
            "unique_id": self.unique_id,
            "is_open": self.is_open,
            "is_invite_only": self.is_invite_only,
            "meeting_location": self.meeting_location,
            "next_meeting_date": self.next_meeting_date,
        }

        new_group_node = Node.cast(AgoraLabel.STUDYGROUP, new_group_properties)
        self.graph_db.create(new_group_node)

        return new_group_node

    def add_interest(self, interest_node):
        """
        link interests to a study group
        :return: list of group interests
        """

        group_interest_relationship = Relationship(start_node=interest_node,
                                                   rel=AgoraRelationship.INTERESTED_IN,
                                                   end_node=self.group_node)

        self.graph_db.create(group_interest_relationship)

        # TODO set properties on RELATIONSHIP
        return self.group_interests

    def update_group(self):
        pass

    def close_group(self):
        pass



