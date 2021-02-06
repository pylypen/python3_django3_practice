# query elasticsearch
import elasticsearch
from elasticsearch_dsl import Search
from django.conf import settings


ELASTIC_HOST = getattr(settings, 'ELASTIC_HOSTS_KEY')
client = elasticsearch.Elasticsearch(hosts=[ELASTIC_HOST])


def perform_lookup(query, index=None, fields=None, internal_sort=True):
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
        elasticsearch_score = hit.meta.score
        hit_score = hit.score
        data = {
            "id": hit.id,
            "title": hit.title,
            "index": hit.meta.index,
            "content": hit.content,
            "url": hit.url,
            "score": elasticsearch_score * hit_score,
        }
        print(data)
        results.append(data)

    if internal_sort:
        results = sorted(results, key=lambda x: x['score'], reverse=True)

    return results
