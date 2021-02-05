# query elasticsearch
import elasticsearch
from elasticsearch_dsl import Search
from django.conf import settings


ELASTIC_HOST = getattr(settings, 'ELASTIC_HOSTS_KEY')
client = elasticsearch.Elasticsearch(hosts=[ELASTIC_HOST])


def perform_lookup(query, index=None, fields=None):
    if index is None:
        index = ["posts", "products"]
    if fields is None:
        fields = ["title", "content"]
    if not query:
        return

    search_results = Search(index=index).using(client).query(
        "multi_match", fields=fields, fuzziness='AUTO',
        query=query
    )
    results = []

    for hit in search_results:
        print(hit.id)
        print(hit.title)
        print(hit.meta.index)
        print(hit.meta.score)
        data = {
            "id": hit.id,
            "title": hit.title,
            "index": hit.meta.index,
            "content": hit.content,
            "url": hit.url,
            "score": hit.meta.score,
        }
        results.append(data)

    return results
