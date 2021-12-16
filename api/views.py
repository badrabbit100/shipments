from rest_framework import status
from api.models import Shipment
from rest_framework.decorators import api_view
from api.serializers import ShipmentSerializer
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def snippet_list(request):
    """ List of All Shipments. Create Shipment by POST request """

    if request.method == 'GET':
        snippets = Shipment.objects.all()
        serializer = ShipmentSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ShipmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk):
    """ Retrieve, update or delete Shipment Object. Allow GET, PUT, DELETE """

    try:
        shipment = Shipment.objects.get(pk=pk)
    except Shipment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ShipmentSerializer(shipment)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ShipmentSerializer(shipment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        shipment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
