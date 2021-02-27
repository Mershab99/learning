from datetime import datetime

from src.mongo.datastore.datastore import Datastore


class ReviewManager:

    def __init__(self):
        self.datastore = ManagerDataStore()

    def create_review(self, user_email, business_email, title, description, rating):
        return self.datastore.create_review(user_email, business_email, title, description, rating)

    def get_all_user_reviews(self, user_email):
        return self.datastore.get_all_user_reviews(user_email)

    def get_all_business_reviews(self, business_email):
        return self.datastore.get_all_business_reviews(business_email)

    def update_review(self, user_email, business_email, title, description, rating):
        return self.datastore.update_review(user_email, business_email, title, description, rating)


class ManagerDataStore(Datastore):
    def __init__(self):
        super().__init__('reviews')

    def __update_fields(self, user_email, fields_to_update):
        return self.collection.update_one(
            {'user_email': user_email},
            {'$set': fields_to_update})

    def create_review(self, user_email, business_email, title, description, rating):
        review = self.collection.insert_one({
            'user_email': user_email,
            'business_email': business_email,
            'title': title,
            'description': description,
            'rating': rating,
            'timestamp': datetime.now().__str__()
        })

        return review is not None

    def update_review(self, user_email, business_email, title, description, rating):
        fields_to_update = {
            'user_email': user_email,
            'business_email': business_email,
            'title': title,
            'description': description,
            'rating': rating,
            'timestamp': datetime.now().__str__()
        }
        self.__update_fields(user_email, fields_to_update)

    def get_all_user_reviews(self, user_email):
        reviews = self.collection.find({
            'user_email': user_email
        }, {'_id': 0})

        return reviews

    def get_all_business_reviews(self, business_email):
        reviews = self.collection.find({
            'business_email': business_email
        }, {'_id': 0})

        return reviews
