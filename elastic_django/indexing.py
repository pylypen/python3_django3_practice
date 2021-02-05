import elasticsearch
from elasticsearch_dsl import Search
import pathlib
import os

ELASTIC_INDEX_NAME = 'cfe-posts'
ELASTICSEARCH_PORT = os.environ.get("ES_PORT", 9200)
ELASTICSEARCH_HOST = os.environ.get("ES_HOST", 'http://127.0.0.1')
ELASTIC_HOST = f'{ELASTICSEARCH_HOST}:{ELASTICSEARCH_PORT}'
print(ELASTIC_HOST)
client = elasticsearch.Elasticsearch(hosts=[ELASTIC_HOST])

post_1 = {
    "id": 1,
    "title": "This is awesome",
    "content": "Here is my date about Django!"
}

post_2 = {
    "id": 2,
    "title": "This is awesome 2",
    "content": "Here is my date about Django!"
}

post_3 = {
    "id": 3,
    "title": "Install guide",
    "content": pathlib.Path("README.md").read_text()
}

client.index(index=ELASTIC_INDEX_NAME, body=post_1)
client.index(index=ELASTIC_INDEX_NAME, body=post_2)
client.index(index=ELASTIC_INDEX_NAME, body=post_3)


if __name__ == "__main__":
    user_query = input("What are you looking for?\n")
    fields = ["title", "content"]
    results = Search(index=ELASTIC_INDEX_NAME).using(client).query(
        "multi_match", fields=fields, fuzziness='AUTO',
        query=user_query
    )
    for hit in results:
        print(hit.id)
        print(hit.title)


