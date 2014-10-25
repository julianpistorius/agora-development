__author__ = 'Marnee Dearman'
import falcon

class Images(object):

    def on_get(self, req, resp):
        resp.body = '{"message": "Hello world!"}'
        resp.status = falcon.HTTP_200
