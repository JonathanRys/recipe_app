#!usr/bin/python
# -*- coding: utf-8 -*-

from elasticsearch_dsl import connections, serializer

class Serializer:
    to_JSON(self, obj):
        return serializer.serializer.loads(obj)

    from_JSON(self, json):
        return serializer.serializer.dumps(json)

# create a class for ES operations
class ES(Serializer):
    __init__(self, host, client='default'):
        self.host = hosts
        self.client = client
        self.connection = self.get_connection()

    get_connection(self):
        # Singleton
        es = connections.get_connections()
        if (es):
            return es
        connections.create_connection(alias=self.client, hosts=[self.host])
        return connections.get_connections()

    loadData(self, index, data):
        # data is stored in flat files so pass a file name here?
        pass

    reindex(self, index):
        pass
