from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Product


@registry.register_document
class ProductDocument(Document):
    url = fields.TextField(attr='get_absolute_url')
    content = fields.TextField(attr='description')

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
