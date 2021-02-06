from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Product


@registry.register_document
class ProductDocument(Document):
    url = fields.TextField(attr='get_absolute_url')
    content = fields.TextField(attr='description')
    score = fields.FloatField(attr="elastic_score")

    class Index:
        """
        Elasticsearch Index
        """
        name = 'products'

    class Django:
        model = Product
        fields = [
            'id',
            'title',
        ]
