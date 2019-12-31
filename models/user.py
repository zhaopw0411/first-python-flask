import sqlite3
from flask_restful import Resource
from db import db

class UserModel(db.Model):
    # it;s an api, are interface to call customer info
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))


    def __init__(self, username, password):
        #self.id = _id --> can delete because we are auto increment id here, don't need to self deflne
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username = username).first()

    @classmethod
    def find_by_userid(cls, id):
        return cls.query.filter_by(id = id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

