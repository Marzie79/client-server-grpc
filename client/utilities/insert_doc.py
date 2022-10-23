from datetime import datetime
from elasticsearch import AsyncElasticsearch


async def insert_doc(service: str, payload: dict):
    """This async function make a new document for an existing index or making a new index"""
    created_at = datetime.now()

    doc = {
        "payload": payload,
        "segment": service,
        "created_at": created_at,
    }
    es = AsyncElasticsearch([{"host": "127.0.0.2", "port": 9200}], http_auth=(
        'elastic', 'changeme'), retry_on_timeout=True)
    await es.index(index=service, body=doc)
#     await es.transport.close()


# from utilities.insert_doc import insert_doc
# import asyncio
# payload = {"name": "it is just a test", "finally": 1}
# loop = asyncio.get_event_loop()
# loop.run_until_complete(insert_doc("funcx", payload))
