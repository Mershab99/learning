from src.mongo.datastore.datastore import Datastore

hours_of_operation_template = {
    'Monday': [],
    'Tuesday': [],
    'Wednesday': [],
    'Thursday': [],
    'Friday': [],
    'Saturday': [],
    'Sunday': [],
}


class BusinessManager:
    def __init__(self):
        self.datastore = BusinessDataStore()

    def create_business(self, email, name, contact_info, detail, hours_of_operation=hours_of_operation_template,
                        service_area={}, service_options=[], menu_images=[]):
        return self.datastore.create_business(email, name, contact_info, detail, hours_of_operation, service_area,
                                              service_options, menu_images)

    def update_business(self, email, name, contact_info, detail, hours_of_operation=hours_of_operation_template,
                        service_area={}, service_options=[], menu_images=[]):
        return self.datastore.update_business(email, name, contact_info, detail, hours_of_operation, service_area,
                                              service_options, menu_images)

    def get_business_card_data(self, email=None, name=None):
        business = self.datastore.get_business(email, name)
        business.pop('detail')
        business.pop('menu_images')
        return business

    def get_business_detail(self, email=None, name=None):
        return self.datastore.get_business(email, name)


class BusinessDataStore(Datastore):
    def __init__(self):
        super().__init__('businesses')

    def __update_fields(self, email, fields_to_update):
        return self.collection.update_one(
            {'email': email},
            {'$set': fields_to_update})

    def create_business(self, email, name, contact_info, detail, hours_of_operation, service_area, service_options,
                        menu_images):
        existing_business = self.collection.find_one({
            'email': email,
            'name': name
        })
        if existing_business:
            raise KeyError("a business with email {} already exists".format(email))

        business = self.collection.insert_one({
            'name': name,
            'email': email,
            'detail': detail,
            'contact_info': contact_info,
            'hours_of_operation': hours_of_operation,
            'service_area': service_area,
            'service_options': service_options,
            'menu_images': menu_images
        })
        return business is not None

    def update_business(self, email, name, contact_info, detail, hours_of_operation, service_area, service_options,
                        menu_images):
        fields_to_update = {
            'name': name,
            'detail': detail,
            'contact_info': contact_info,
            'hours_of_operation': hours_of_operation,
            'service_area': service_area,
            'service_options': service_options,
            'menu_images': menu_images
        }
        return self.__update_fields(email, fields_to_update)

    def get_business(self, email=None, name=None):
        if email is None and name is None:
            raise KeyError("No email or name provided")
        elif email is not None:
            business = self.collection.find_one({
                'email': email
            }, {'_id': 0})
        else:
            business = self.collection.find_one({
                'name': name
            }, {'_id': 0})
        #business.pop('_id')
        return business
