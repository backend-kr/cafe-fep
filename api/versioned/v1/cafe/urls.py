from django.urls import path
from .views import KAKAOCafeViewSet, NaverCafeViewSet

urlpatterns = [
    path('kakao/', KAKAOCafeViewSet.as_view({'post': 'retrieve'})),
    path('naver/', NaverCafeViewSet.as_view({'post': 'retrieve'}))
]
