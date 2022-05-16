from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import mapper
from .db import metadata, db_session

class User(object):
    query = db_session.query_property()

    def __init__(self, first_name=None,last_name=None, username=None,bio=None, email=None):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.bio = bio
        self.email = email

    def __repr__(self):
        return f'<User {self.name!r}>'

users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('first_name', String(50), unique=True),
    Column('last_name', String(50), unique=True),
    Column('username', String(50), unique=True),
    Column('bio', String(50), unique=True),
    Column('email', String(120), unique=True)
)
mapper(User, users)