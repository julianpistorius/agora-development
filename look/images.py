__author__ = 'Marnee Dearman'
import falcon

class Resource(object):

    def on_get(selfself, req, resp):
        resp.body = '{"message": "Hello World!"}'
        resp.status = falcon.HTTP_200
