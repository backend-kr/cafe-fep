from rest_framework import serializers

from api.versioned.v1.cafe import output_serializers
from api.versioned.v1.cafe.serializers import AdapterMixin
from api.versioned.v1.common.adapter import kakao_openapi_adapter, naver_openapi_adapter


class KaKaoCafeListReqSerializer(AdapterMixin, serializers.Serializer):
    adapter = kakao_openapi_adapter
    endpoint = "/v2/local/search/category.json"

    response_serializer_class = output_serializers.KakaoListRespSerializer

    page = serializers.HiddenField(default=1,help_text='페이지')
    size = serializers.HiddenField(default=15, help_text='사이즈')
    sort = serializers.HiddenField(default='accuracy', help_text='분류')
    category_group_code = serializers.HiddenField(default="CE7", help_text='코드')
    latitude = serializers.DecimalField(default=37.690235357826, max_digits=20, decimal_places=16, source="y", help_text='위도')
    longitude = serializers.DecimalField(default=126.71946531058, max_digits=20, decimal_places=16, source="x", help_text='경도')


class NaverCafeListReqSerializer(AdapterMixin, serializers.Serializer):
    adapter = naver_openapi_adapter
    endpoint = "/v5/api/search"

    response_serializer_class = output_serializers.NaverListRespSerializer

    caller = serializers.CharField(default='pcweb', help_text='요청 기기')
    query = serializers.CharField(default="연신내", help_text='지역')
    page = serializers.CharField(default='1', help_text='페이지')
    type = serializers.CharField(default='all', help_text='타입')
    recommandation = serializers.CharField(default="true", source='isPlaceRecommendationReplace', help_text='추천')
    latitude = serializers.CharField(default='37.6943312', help_text='위도')
    longitude = serializers.CharField(default='126.764245', help_text='경도')
    display_count = serializers.IntegerField(default=1, source='displayCount', help_text='요청 개수', min_value=1,
                                             max_value=300)
    lang = serializers.CharField(default='ko', help_text='언어')


    def to_internal_value(self, data):
        data = super().to_internal_value(data=data)
        data['query'] = data['query'] + ' 카페'
        return data


class NaverCafeDetailReqSerializer(AdapterMixin, serializers.Serializer):
    adapter = naver_openapi_adapter
    endpoint = "/v5/api/sites/summary/{cafe_id}"

    response_serializer_class = output_serializers.NaverCafeDetailRespSerializer

    cafe_id = serializers.CharField(default='1506083152', help_text='카페 아이디')
    lang = serializers.CharField(default='ko', help_text='언어')


