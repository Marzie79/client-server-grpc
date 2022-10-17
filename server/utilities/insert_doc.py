from datetime import datetime
from elasticsearch import Elasticsearch


def insert_doc(service: str, payload: dict):
    created_at = datetime.now()

    doc = {
        "payload": payload,
        "segment": service,
        "created_at": created_at,
    }
    es = Elasticsearch([{"host": "127.0.0.2", "port": 9200}], http_auth=('elastic', 'changeme'))
    es.index(index="test", body=doc)