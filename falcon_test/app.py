__author__ = 'Marnee Dearman'
import falcon
import os
import images

api = application = falcon.API()
path = os.path.abspath('files')
print path
images = images.Resource(path)
api.add_route('/images', images)