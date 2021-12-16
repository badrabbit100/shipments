from django.urls import path, include
from api import views


urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('shipments/', views.snippet_list),
    path('shipments/<int:pk>/', views.snippet_detail),
]