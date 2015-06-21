""" Cornice services.
"""
from cornice.resource import resource
from reactions.models import (
    DBSession,
)



@resource(collection_path='/userapp', path='/userapp/{key}')
class UserApp(object):

    def __init__(self, request):
        self.request = request

    def get(self):
        name = self.request.matchdict['key']

    def collection_post(self):
        self.request.response.status_code = 201
        return {
            'APIKey': 'apikey',
            'SecretKey': 'secretkey'
        }
