from rest_framework import viewsets, permissions
from api.versioned.v1.cafe import input_serializers
from common.viewsets import RetrieveModelMixin, MappingViewSetMixin


class CafeBaseViewSet(MappingViewSetMixin,
                      viewsets.GenericViewSet,
                      ):
    permission_classes = [permissions.AllowAny]
    # filter_backends = (filters.DjangoFilterBackend,)
    filter_class = None
    serializer_class = None

    def get_queryset(self):
        return None

class KAKAOCafeViewSet(RetrieveModelMixin, CafeBaseViewSet):
    """
    retrieve: kakao open api

    kakao open api 카페 리스트 반환
    """

    filter_class = None
    serializer_class = input_serializers.KaKaoCafeListReqSerializer

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class NaverCafeViewSet(RetrieveModelMixin, CafeBaseViewSet):
    """
    retrieve: 네이버 크롤링

    네이버 크롤링 카페 리스트 반환
    ### endpoint : `/v5/api/search`

    ### 거래 구분(display_count) Min: 1, MAX: 300

    """

    filter_class = None
    serializer_class = input_serializers.NaverCafeListReqSerializer

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)