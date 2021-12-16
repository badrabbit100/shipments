from api.models import Shipment
from rest_framework import serializers


class ShipmentSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer for Shipment objects """

    class Meta:
        model = Shipment
        fields = ('id', 'name', 'description', 'amount', 'price', )
