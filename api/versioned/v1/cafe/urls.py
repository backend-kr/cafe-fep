from django.urls import path
from .views import KAKAOCafeViewSet, NaverCafeViewSet, NaverCafeDetailViewSet

urlpatterns = [
    path('kakao', KAKAOCafeViewSet.as_view({'post': 'retrieve'})),
    path('naver/sites', NaverCafeViewSet.as_view({'post': 'retrieve'})),
    path('naver/site-detail', NaverCafeDetailViewSet.as_view({'post': 'retrieve'}))
]
