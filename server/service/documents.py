from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from elasticsearch_dsl import analyzer

from service.models import Stuff

html_strip = analyzer(
    'html_strip',
    tokenizer='standard',
    filter=['standard', 'lowercase', 'stop', 'snowball'],
    char_filter=['html_strip']
)


@registry.register_document
class StuffDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'stuff'
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    id = fields.KeywordField()
    name = fields.TextField()
    service = fields.KeywordField()
    created_at = fields.DateField()
    updated_at = fields.DateField()

    class Django:
        model = Stuff

# sudo docker run -d --name service_elas -p9200:9200 -p9300:9300 -e 'discovery.type=single-node' -e xpack.security.enabled=false -v esdata:/usr/share/elasticsearch/data elasticsearch:8.4.3

