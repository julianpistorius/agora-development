__author__ = 'Marnee Dearman'
import os
import time
import uuid
import falcon
import msgpack_pure

def _media_type_to_ext(media_type):
    # Strip off the 'image/' prefix
    return media_type[6:]

def _generate_id():
    return str(uuid.uuid4())

class Resource(object):

    def __init__(self, storage_path):
        self.storage_path = storage_path

    def on_get(selfself, req, resp):
        resp.data = msgpack_pure.packb({'message': 'Hello world!'})
        resp.content_type = 'application/msgpack'
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        image_id = _generate_id()
        ext = _media_type_to_ext(req.content_type)
        filename = image_id + '.' + ext

        image_path = os.path.join(self.storage_path, filename)

        with open(image_path, 'wb') as image_file:
            while True:
                chunk = req.stream.read(4096)
                if not chunk:
                    break

                image_file.write(chunk)
        image_file.close()
        resp.status = falcon.HTTP_201
        resp.location = '/images/' + image_id