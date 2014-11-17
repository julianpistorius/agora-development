__author__ = 'Marnee Dearman'
import py2neo
import uuid
import collections
from py2neo import neo4j
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
        self.graph_db = neo4j.Graph("http://localhost:7474/db/data/")

    @property
    def group_node(self):
        """
        get a group node based on the unique id attribute
        :return: neo4j.Node
        """
        return self.graph_db.get_or_create_indexed_node(index_name=AgoraLabel.STUDYGROUP,
                                                        key='unique_id',
                                                        value=self.unique_id)

    @property
    def group_interests(self):
        """ get user interests
        :return: list of interests
        """
        group_interests = self.graph_db.match(start_node=self.group_node,
                                              rel_type=AgoraRelationship.INTERESTED_IN,
                                             end_node=None)
        #create a list of tuples of interests and the users's relationship to them
        interests_list = []
        for item in group_interests:
            interests_list.append((item.end_node["name"], item["description"]))
        # return [item.end_node["name"] for item in user_interests]
        return interests_list

    def create_group(self):
        """
        create new study group or circle
        :return:
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
        new_group = self.graph_db.get_or_create_indexed_node(index_name=AgoraLabel.STUDYGROUP,
                                                             key='name', value=self.name,
                                                             properties=new_group_properties)
        new_group.add_labels(AgoraLabel.STUDYGROUP)
        return new_group

    def add_interest(self, interest_id, interest_description):
        """
        link interests to a study group
        :return:
        """
        interest_node = self.graph_db.get_indexed_node(index_name=AgoraLabel.INTEREST,
                                                       key='unique_id', value=interest_id)
        #CREATE the RELATIONSHIP BETWEEN INTEREST AND GROUP
        neo4j.Path(self.group_node, AgoraRelationship.INTERESTED_IN,
                   interest_node).get_or_create(graph_db=self.graph_db)
        #TODO set properties on RELATIONSHIP

    def update_group(self):
        pass

    def close_group(self):
        pass



