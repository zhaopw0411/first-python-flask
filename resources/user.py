import sqlite3
from flask_restful import Resource, reqparse 
from models.user import UserModel



# it's a resource class
class UserRegister(Resource):
    # only pass certain thing / argument
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help='This field cannot be left blank')

    parser.add_argument('password',
        type=str,
        required=True,
        help='This field cannot be left blank')

        
    def post(self):
        data = UserRegister.parser.parse_args()
        
        # user already exists
        if UserModel.find_by_username(data['username']):
            return {"message": "User already registered"}, 400
        else:
            user = UserModel(**data) #UserModel(data['username'], data['password'])
            user.save_to_db()
            return {"message": "User created successfully"}, 201