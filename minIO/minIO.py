from minio import Minio
from minio.error import InvalidResponseError

client = Minio("localhost:9000", "learning", "test12345", secure=False)

BUCKET_NAME = "dev1"


class ObjectStorage:
    client = client

    def create_bucket(self):
        if not client.bucket_exists(BUCKET_NAME):
            client.make_bucket(BUCKET_NAME)

    def put_img(self, obj_name, obj_loc):
        try:
            client.fput_object(BUCKET_NAME, obj_name, obj_loc, content_type='image/jpeg')
        except InvalidResponseError as err:
            print(err)

    def get_obj(self, obj_name, obj_loc=None):
        try:
            return client.get_object(BUCKET_NAME, obj_name, obj_loc)
        except InvalidResponseError as err:
            print(err)

    def get_obj_url(self, obj_name):
        return client.presigned_get_object(BUCKET_NAME, obj_name)
    # def list_obj(self, bucket):
    #    objects =


# TODO: add this to startup script
ObjectStorage().create_bucket()

'''
class UploadImage(Resource):
   def post(self):
     parse = reqparse.RequestParser()
     parse.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
     args = parse.parse_args()
     image_file = args['file']
     image_file.save("your_file_name.jpg")
'''
