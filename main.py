import hug
import os
import psycopg2
from urllib.parse import urlparse

url = urlparse(os.environ["DATABASE_URL"])

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)

@hug.get()
def hello():
  '''Says hello'''
  return 'Hello!'

@hug.get()
def get_clusters():
  '''return a list of clusters'''
  clusters = [{'name': 'test', 'size': 'small'},{'name': 'prod', 'size': 'large'}]
  return clusters
