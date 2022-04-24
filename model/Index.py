from operator import index
from pydoc import cli
from elasticsearch import Elasticsearch
from model.service import auth
from os import environ


def read():
    es_header, basic_auth = auth.get_es_headers()
    client = Elasticsearch(es_header, http_auth=basic_auth)
    connected = client.ping()
    index = client.indices.get(index="*")
    response = {
        "connected": connected,
        "index": index
    }

    return response, 200
