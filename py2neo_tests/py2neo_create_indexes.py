__author__ = 'Marnee Dearman'
import py2neo
import uuid
import collections
from py2neo import neo4j
from agora_db.agora_types import AgoraRelationship, AgoraLabel

graph_db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")
graph_db.get_or_create_index(content_type=neo4j.Relationship,
                             index_name=AgoraRelationship.INTERESTED_IN)
graph_db.get_or_create_index(content_type=neo4j.Relationship,
                             index_name=AgoraRelationship.HAS_GOAL)
graph_db.get_or_create_index(content_type=neo4j.Relationship,
                             index_name=AgoraRelationship.ACHIEVED)
graph_db.get_or_create_index(content_type=neo4j.Relationship,
                             index_name=AgoraRelationship.GOAL_INTEREST)
graph_db.get_or_create_index(content_type=neo4j.Relationship,
                             index_name=AgoraRelationship.MEMBER_OF)
graph_db.get_or_create_index(content_type=neo4j.Relationship,
                             index_name=AgoraRelationship.SPECIALIZED_IN)
graph_db.get_or_create_index(content_type=neo4j.Relationship,
                             index_name=AgoraRelationship.IS_A)
graph_db.get_or_create_index(content_type=neo4j.Relationship,
                             index_name=AgoraRelationship.STUDIES)
graph_db.get_or_create_index(content_type=neo4j.Relationship,
                             index_name=AgoraRelationship.LEARNING)
graph_db.get_or_create_index(content_type=neo4j.Relationship,
                             index_name=AgoraRelationship.LOCATED_IN)
graph_db.get_or_create_index(content_type=neo4j.Relationship,
                             index_name=AgoraRelationship.LEADS)



