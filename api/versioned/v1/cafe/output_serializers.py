import arrow
from django.conf import settings
from rest_framework import serializers


def get_arrow_datetime(value):
    date_part = value[:8]
    time_part = value[8:]

    date = arrow.get(date_part, 'YYYYMMDD')

    hours = int(time_part[:2])
    minutes = int(time_part[2:])

    if hours >= 24:
        days_to_add = hours // 24
        hours %= 24

        date = date.shift(days=days_to_add).replace(hour=hours, minute=minutes)
    else:
        date = date.replace(hour=hours, minute=minutes)

    return date.format('HH:mm')
class KakaoListRespSerializer(serializers.Serializer):
    class CafeListDataSerializer(serializers.Serializer):
        address_name = serializers.CharField(default='', help_text="주소")
        category_group_code = serializers.HiddenField(default='', help_text="카테고리 분류")
        category_group_name = serializers.HiddenField(default='', help_text="카테고리 이름")
        category_group_tree = serializers.HiddenField(default='', source="category_name", help_text="카테고리 이름")
        id = serializers.HiddenField(default='', help_text="id")
        distance = serializers.CharField(default='', help_text="거리")
        phone_number = serializers.CharField(default='', source="phone", help_text="전화 번호")
        cafe_name = serializers.CharField(default='', source="place_name", help_text="카페 이름")
        cafe_url = serializers.CharField(default='', source="place_url", help_text="카페 url")
        road_address_name = serializers.CharField(default='', help_text="길 주소")
        latitude = serializers.CharField(default='', source='y', help_text='위도')
        longitude = serializers.CharField(default='', source='x', help_text='경도')
    documents = CafeListDataSerializer(many=True)





class NaverCafeDetailRespSerializer(serializers.Serializer):
    class NaverCafeDetailOptionDataSerializer(serializers.Serializer):
        """Naver Cafe Detail DataSerializer"""
        option_id = serializers.CharField(default='', source='id', help_text='편의 옵션 아이디')
        option_name = serializers.CharField(default='', source='name', help_text='편의 옵션 이름')

    class NaverCafeMenuImagesSerializer(serializers.Serializer):
        """Naver Cafe Menu Image Detail DataSerializer"""
        image_url = serializers.CharField(default='', source="imageUrl", help_text='카페 홈페이지')

    id = serializers.CharField(default='', help_text='카페 아이디')
    cafe_name = serializers.CharField(default='', source="name", help_text='검색 전체 개수')
    description = serializers.CharField(default='', help_text='검색 전체 개수')
    parking_support = serializers.BooleanField(default=False, source='isParkingSupported')
    categories = serializers.ListField(child=serializers.CharField())
    options = NaverCafeDetailOptionDataSerializer(many=True)
    menu_images = NaverCafeMenuImagesSerializer(source='menuImages', many=True)
    review_count = serializers.IntegerField(default=0, source='reviewCount', help_text='리뷰 갯수')

class NaverBaseListRespSerializer(serializers.Serializer):
    class NaverBaseDataSerializer(serializers.Serializer):
        """Naver 위치 DataSerializer"""
        cafe_id = serializers.CharField(default='', source='id', help_text='카페 아이디')
        menu_info = serializers.CharField(default='', source='menuInfo', help_text='카페 메뉴')
        tel = serializers.CharField(help_text='카페 번호')
        thumUrls = serializers.ListField(child=serializers.CharField())
        title = serializers.CharField(default='', source='display', help_text='카페 이름')
        review_count = serializers.CharField(default='', source='reviewCount', help_text='카페 이름')
        place_review_count = serializers.CharField(default='', source='placeReviewCount', help_text='카페 이름')
        address = serializers.CharField(default='')
        road_address = serializers.CharField(default='', source='roadAddress', help_text='카페 주소 1')
        business_hours = serializers.CharField(default='', source='businessStatus.businessHours', help_text='카페 주소 2')
        latitude = serializers.CharField(default='', source='y', help_text='위도')
        longitude = serializers.CharField(default='', source='x', help_text='경도')
        home_page = serializers.CharField(default='', source="homePage", help_text='카페 홈페이지')

    total_count = serializers.IntegerField(default='', source="result.place.totalCount", help_text='검색 전체 개수')
    result = NaverBaseDataSerializer(source='result.place.list', many=True)


class NaverRestaurantListRespSerializer(NaverBaseListRespSerializer):
    """음식점 OutputSerializer"""


class NaverCafeListRespSerializer(NaverBaseListRespSerializer):
    """카페 OutputSerializer"""
    def to_representation(self, instance):
        instance = super().to_representation(instance=instance)
        result = instance.get('result', None)
        for _result in result:
            business_hours = _result.pop('business_hours')
            start_time_str, end_time_str = business_hours.split('~')
            _result['business_hours_start'] = get_arrow_datetime(start_time_str)
            _result['business_hours_end'] = get_arrow_datetime(end_time_str)
        return instance


class NaverAttractionListRespSerializer(NaverBaseListRespSerializer):
    """명소 OutputSerializer"""