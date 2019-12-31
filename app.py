from flask import Flask, request
from flask_restful import Api
from flask_jwt import JWT # for authentication


from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, Items
from resources.store import Store, StoreList # squalchemy will auto create the tables that imported

from db import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'key'
api = Api(app)

db.init_app(app)

# auto create tables before other request
@app.before_first_request
def create_tables():
    db.create_all()


# JWT create a new endpoint /auth
jwt = JWT(app, authenticate, identity)


# let our api student be accessible   
api.add_resource(StoreList, '/stores')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Items, '/items') 
api.add_resource(Item, '/item/<string:name>') 
api.add_resource(UserRegister, '/register')

## http://127.0,0.1:5000/studemt/Rolf -> same as the decorator

if __name__ == '__main__':
    app.run(port=5000, debug=True)