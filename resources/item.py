from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from models.item import ItemModel

class Items(Resource):
    def get(self):
        return {'items': [item.json()for item in ItemModel.query.all()]}
        # = list(map(lambda x:x.json(), ItemModel.query.all()))

class Item(Resource):
    # only pass certain thing / argument
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help='This field cannot be left blank')
    
    parser.add_argument('store_id',
        type=float,
        required=True,
        help='Every item need a store id')


    @jwt_required()
    # dont need @app.route decorator here.
    def get(self, name):
        item = ItemModel.find_by_name(name) # or Item.find_..., the same
        if item:
            return item.json() #return an item itself instead of a object
        return {"message": "Item not found"}, 404



    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400
            # 400 is bad request
        
        request_data = Item.parser.parse_args()

        #item = ItemModel(name, request_data['price'], request_data['store_id'])
        item = ItemModel(name,**request_data)
        
        try:
            item.save_to_db()
        except:
            return {"message" : "An message occurred inserting the item"}, 500 # internal server error
        return item.json(), 201
        # 201 is for item already created



    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()


    def put(self, name):
        request_data = Item.parser.parse_args()
        
        item = ItemModel.find_by_name(name)

        if item is None:
            #item = ItemModel(name, request_data['price'], request_data['store_id'])
            item = ItemModel(name,**request_data)
        else:
            item.price = request_data['price']

        item.save_to_db()


        return item.json()