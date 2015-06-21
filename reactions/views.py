""" Cornice services.
"""
import transaction
from cornice.resource import resource

from reactions.models import DBSession

from reactions import models


@resource(collection_path='/userapp', path='/userapp/{api_key}')
class UserAppResource(object):

    def __init__(self, request):
        self.request = request

    def get(self):
        api_key = self.request.matchdict['api_key']

        user_app = DBSession.query(
            models.UserApp
        ).filter(models.UserApp.api_key == api_key).one()

        return {
            'APIKey': user_app.api_key,
            'SecretKey': user_app.secret_key
        }

    def collection_post(self):
        self.request.response.status_code = 201

        user_app = models.UserApp(
            api_key='apikey',
            secret_key='secretkey'
        )
        with transaction.manager:
            DBSession.add(
                user_app
            )
            return {
                'APIKey': user_app.api_key,
                'SecretKey': user_app.secret_key
            }
