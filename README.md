Client & Server service


# Running ElasticSearch

`docker run -d --name service_elas -p9200:9200 -p9300:9300 -e 'discovery.type=single-node' -e xpack.security.enabled=false -v esdata:/usr/share/elasticsearch/data elasticsearch:8.4.3`

# Install requirements

`pip install -r requirements.txt `

# In server project run grpc server

`python manage.py grpcserver --port 50151`

you can set any port that you want

# In client project start server

`python manage.py runserver`
