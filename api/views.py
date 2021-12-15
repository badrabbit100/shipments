from api.models import Shipment
from api.serializers import ShipmentSerializer
from rest_framework import viewsets


class ShipmentViewSet(viewsets.ModelViewSet):
    """ ViewSet provide GET, POST, DELETE, UPDATE methods to Shipment objects  """

    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
