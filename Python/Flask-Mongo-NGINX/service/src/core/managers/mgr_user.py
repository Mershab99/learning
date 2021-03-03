from datetime import datetime

from src.mongo.datastore.datastore import Datastore

class UserManager:

    def __init__(self):
        self.datastore = UserDataStore()

    def login(self, email, password, loc):
        return self.datastore.login(email, password, loc)

    def create_user(self, email, name, password, loc):
        return self.datastore.create_user(email, name, password, loc)

    def update_user(self, email, name, password, loc):
        return self.datastore.update_user(email, name, password, loc)


class UserDataStore(Datastore):
    def __init__(self):
        super().__init__('users')

    def __update_fields(self, email, fields_to_update):
        return self.collection.update_one(
            {'email': email},
            {'$set': fields_to_update})

    def create_user(self, email, name, password, loc):
        existing_user = self.collection.find_one({
            'email': email
        })
        if existing_user:
            raise KeyError("a user with email {} already exists".format(email))

        user = self.collection.insert_one({
            'email': email,
            'name': name,
            'password': password,
            'last_login_location': loc,
            'last_login_timestamp': datetime.now().__str__()
        })

        return user is not None

    def login(self, email, password, loc):
        user = self.collection.find_one({
            'email': email,
            'password': password
        })
        if user:
            fields_to_update = {
                'last_login_location': loc,
                'last_login_timestamp': datetime.now().__str__()
            }
            self.update_fields(email, fields_to_update)
            return True
        else:
            return False

    def update_user(self, email, name, password, loc):
        fields_to_update = {
            'email': email,
            'name': name,
            'password': password,
            'last_login_location': loc,
            'last_login_timestamp': datetime.now().__str__()
        }
        self.__update_fields(email, fields_to_update)
