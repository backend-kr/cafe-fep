import requests
# BASE_URL = https://dapi.kakao.com
# ENDPOINT = /v2/local/search/category.json
# queryset = category_group_code=CE7&page=1&size=15&sort=accuracy&x=126.71946531058&y=37.690235357826
# queryset 설명
# category_group_code - 히위 정리
# sort - distance 또는 accuracy (기본값: accuracy)
# x - 경도
# y - 위도

"""
MT1	대형마트
CS2	편의점
PS3	어린이집, 유치원
SC4	학교
AC5	학원
PK6	주차장
OL7	주유소, 충전소
SW8	지하철역
BK9	은행
CT1	문화시설
AG2	중개업소
PO3	공공기관
AT4	관광명소
AD5	숙박
FD6	음식점
CE7	카페
HP8	병원
PM9	약국
"""
url = "https://dapi.kakao.com/v2/local/search/category.json"
header = {'Content-Type': 'application/json', 'Authorization': 'KakaoAK 85aac2a4ebbc7ac02d7a26e7e377ee28'}
params = {
    "category_group_code": "CE7",
    "page": 1,
    "size": 15,
    "sort": "accuracy",
    "x": 126.71946531058,
    "y": 37.690235357826
}
response = requests.request("GET", url, headers=header, params=params)
tokens = response.json()

print(response)
print(tokens)

