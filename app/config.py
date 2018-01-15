import os


class app:
    secret_key = 'super secret string 228'


class db:
    user = os.environ['POSTGRES_USER']
    pw = os.environ['POSTGRES_PASSWORD']
    db = os.environ['POSTGRES_DB']
    host = 'db'
    port = '5432'
    uri = 'postgresql://{}:{}@{}:{}/{}'.format(user, pw, host, port, db)
