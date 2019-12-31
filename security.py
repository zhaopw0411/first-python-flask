from werkzeug.security import safe_str_cmp
from models.user import UserModel

# in memory db
# users = [
#     {
#         'id': 1,
#         'user_name': 'bob',
#         'password':'asdf'
#     }
# ]

# username_mapping = {
#     'bob':
#         {
#             'id': 1,
#             'user_name': 'bob',
#             'password':'asdf'
#         }
# }

# userid_mapping = {
#     1 :
#         {
#             'id': 1,
#             'user_name': 'bob',
#             'password':'asdf'
#         }
# }

# users = [User(1,'bob','asdf')]

# username_mapping = {u.username: u for u in users}

# userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
    #user = username_mapping.get(username, None)
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password): #user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_userid(user_id)
    #return userid_mapping.get(user_id, None)