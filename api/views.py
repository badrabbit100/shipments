from api.models import Shipment
from api.serializers import ShipmentSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response


class ShipmentViewSet(viewsets.ModelViewSet):
    """ ViewSet provide GET, POST, DELETE, UPDATE methods to Shipment objects  """

    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
