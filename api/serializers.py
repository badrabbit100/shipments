from api.models import Shipment
from rest_framework import serializers


class ShipmentSerializer(serializers.HyperlinkedModelSerializer):
    """ Serialization class for Shipment objects """

    class Meta:
        model = Shipment
        fields = ['name', 'description', 'amount', 'price']
