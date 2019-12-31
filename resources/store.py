from flask_restful import Resource, reqparse
from models.store import StoreModel



class Store(Resource):
    # only pass certain thing / argument
    parser = reqparse.RequestParser()
    parser.add_argument('name',
        type=float,
        required=True,
        help='This field cannot be left blank')
    
    parser.add_argument('store_id',
        type=float,
        required=True,
        help='Every item need a store id')


    def get(self, name):
        store = StoreModel.find_by_name(name) # or Item.find_..., the same
        if store:
            return store.json() #return an item itself instead of a object
        return {"message": "Store not found"}, 404



    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': "An store with name '{}' already exists.".format(name)}, 400
            # 400 is bad request
    
        store = StoreModel(name)
        
        try:
            store.save_to_db()
        except:
            return {"message" : "An message occurred inserting the store"}, 500 # internal server error
        return store.json(), 201
        # 201 is for item already created



    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {'message': 'Store deleted'}

class StoreList(Resource):
    def get(self):
        return {'stores': [store.json()for store in StoreModel.query.all()]}