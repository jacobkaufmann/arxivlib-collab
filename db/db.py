import os
from json import dumps

from neo4j import GraphDatabase, basic_auth

passwd = os.getenv("NEO4J_PASSWORD")
driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", passwd))

def get_db():
    return driver.session()