from rest_framework import routers
from api.views import ShipmentViewSet


router = routers.DefaultRouter()

router.register(r'shipments', ShipmentViewSet)
