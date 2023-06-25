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
    retrieve: kakao open api(K8S를 테스트를 위해 주석 생성해봄)

    kakao open api 카페 리스트 반환 K8S 
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

    ### 요청 구분(display_count) Min: 1, MAX: 300

    """

    filter_class = None
    serializer_class = input_serializers.NaverCafeListReqSerializer

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class NaverCafeDetailViewSet(RetrieveModelMixin, CafeBaseViewSet):
    """
    retrieve: 네이버 카페 디테일 크롤링

    네이버 크롤링 카페 디테일 리스트 반환
    ### endpoint : `/v5/api/sites/summary/{cafe_id}`


    """

    filter_class = None
    serializer_class = input_serializers.NaverCafeDetailReqSerializer

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)