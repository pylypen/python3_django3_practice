import os

ELASTICSEARCH_PORT = os.environ.get("ES_PORT", 9200)
ELASTICSEARCH_HOST = os.environ.get("ES_HOST", 'http://127.0.0.1')
ELASTIC_HOSTS_KEY = f'{ELASTICSEARCH_HOST}:{ELASTICSEARCH_PORT}'

ELASTICSEARCH_DSL = {
    'default': {
        'hosts': ELASTIC_HOSTS_KEY
    }
}
