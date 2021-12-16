from api.models import Shipment
from django.contrib.auth.models import User
import random, os


def create_shipments_in_database(amount_new_objects):
    """ Create random testing-objects in database """

    for i in range(1, amount_new_objects + 1):
        Shipment.objects.create(name=f'Test Object #{i}',
                                description=f'Test Description for shipments #{i}',
                                amount=random.randrange(100, 1000),
                                price=random.randrange(500, 25000),
                                )


def create_super_user():
    """ Create SuperUser in Database """

    User.objects.create_superuser(username='admin', password='superadmin1234')


def main():
    """ Quick Init Database
    $ echo "from init_db import main; main(); exit()" | python3 manage.py shell
    """
    create_shipments_in_database(amount_new_objects=10)
    create_super_user()
