from sqlalchemy import Column, Integer, String
from app.extensions import db


class User(db.Model):
    __table_name__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(30), unique=True, nullable=False)
    password = Column(String(1000), nullable=False)


    def __init__(self, username, password):
        self.username = username
        self.password = password
