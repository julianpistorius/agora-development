__author__ = 'Marnee Dearman'
import falcon
import images

api = application = falcon.API()

images = images.Images()
api.add_route('/images', images)