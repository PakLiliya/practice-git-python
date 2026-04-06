import psycopg2
from configpb import load_config

def get_connection():
    config = load_config()
    return psycopg2.connect(**config)