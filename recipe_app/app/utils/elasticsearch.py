#!usr/bin/python
# -*- coding: utf-8 -*-

from elasticsearch_dsl import connections, serializer

class Serializer:
    def to_JSON(self, obj):
        return serializer.serializer.loads(obj)

    def from_JSON(self, json):
        return serializer.serializer.dumps(json)

# create a class for ES operations
class ES(Serializer):
    def __init__(self, host, client='default'):
        self.host = hosts
        self.client = client
        self.connection = self.get_connection()

    def get_connection(self):
        # Singleton
        es = connections.get_connections()
        if (es):
            return es
        connections.create_connection(alias=self.client, hosts=[self.host])
        return connections.get_connections()

    def loadData(self, index, data):
        # data is stored in flat files so pass a file name here?
        pass

    def reindex(self, index):
        pass
