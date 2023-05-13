from django.urls import path
from .views import StatusViewSet

urlpatterns = [
    path('health-check', StatusViewSet.as_view({'get': 'status'}))
]
