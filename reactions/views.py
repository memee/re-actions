""" Cornice services.
"""
from cornice import Service
from reactions.models import (
    DBSession, MyModel
)


hello = Service(name='hello', path='/', description="Simplest app")


@hello.get()
def get_info(request):
    """Returns Hello in JSON."""
    model = DBSession.query(MyModel).one()
    return {model.name: model.value}
