from src.core.managers.mgr_business import BusinessDataStore


class MapManager:
    def get_map(self, box, service_options):
        # Modify to filter service options : OPEN NOW
        businesses = BusinessDataStore().collection.find({
            # Find all businesses inside the box.
            # box.x1,x2,y1,y2
            'service_area.lat': {
                '$gte': box.x1,
                '$lte': box.x2},
            'service_area.lng': {
                '$gte': box.y1,
                '$lte': box.y2},
            'service_options': {'$in': service_options}
        }, {'_id': 0})
        return businesses
