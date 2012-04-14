import pymongo
import os

from pymongo.uri_parser import parse_uri
from unittest import TestCase

class MongoDBIntegrationTest(TestCase):

    def setUp(self):
        # Fetch the Strider MongoDB URI from the environment if available.
        # Otherwise default to localhost/testdb
        mongodb_uri = os.getenv('MONGODB_URI', "mongodb://localhost/testdb")
        parsed_db_uri = parse_uri(mongodb_uri)

        username = parsed_db_uri.get("username")
        password = parsed_db_uri.get("password")
        database = parsed_db_uri.get("database")
        conn = pymongo.Connection(host="localhost",
                port=int(parsed_db_uri["nodelist"][0][1]))
        if username and password:
            conn[database].authenticate(username, password)

        self.db = conn[database]

    def test_write_and_read(self):
        doc = {"key":"my key!", "value":"a value"}
        self.db["test"].insert(doc, safe=True)
        r = self.db["test"].findOne({"key":doc["key"]})
        assert r == doc
