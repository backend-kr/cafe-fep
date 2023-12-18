from rest_framework import viewsets, permissions
from api.versioned.v1.cafe import input_serializers
from api.versioned.v1.cafe.output_serializers import NaverBaseListRespSerializer
from common.viewsets import RetrieveModelMixin, MappingViewSetMixin
from drf_yasg.utils import swagger_auto_schema


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

    ### 요청 구분(display_count) Min: 1, MAX: 300

    """

    filter_class = None
    serializer_class = input_serializers.NaverCafeListReqSerializer

    @swagger_auto_schema(
        responses={200: NaverBaseListRespSerializer},
        operation_summary="네이버 카페, 식당, 명소 크롱링 API",
        operation_description="네이버에서 카페, 식당, 명소를 크롤링."
    )
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