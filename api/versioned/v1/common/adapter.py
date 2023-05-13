from urllib.parse import urljoin

from api.versioned.v1.common.base import APIRequest
from api_backend import settings
from common.designpatterns import dotdict, SingletonClass

__all__ = ["kakao_openapi_adapter", "kakao_settings",
           "naver_openapi_adapter", "naver_settings"]

kakao_settings = dotdict(settings.KAKAO_CLIENT)
naver_settings = dotdict(settings.NAVER_CLIENT)

class KakaoAdapterClass(SingletonClass):
    __base = kakao_settings.KAKAO_BASE_URL
    __token = kakao_settings.KAKAO_API_TOKEN

    def request(self, additional_url=None, body=None, headers=None, method='GET', timeout=None):
        requester = APIRequest(url=urljoin(self.__base, additional_url), headers=headers, body=body)
        requester.update_headers({"Authorization": f"KakaoAK {self.__token}"})
        response = requester.send(method=method)
        return response


class NaverAdapterClass(SingletonClass):
    __base = naver_settings.NAVER_BASE_URL

    def request(self, additional_url=None, body=None, headers=None, method='GET', timeout=None):
        requester = APIRequest(url=urljoin(self.__base, additional_url), headers=headers, body=body)
        requester.update_headers({
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
                'Referer': 'https://map.naver.com/'
            })
        response = requester.send(method=method)
        return response

kakao_openapi_adapter = KakaoAdapterClass.instance()
naver_openapi_adapter = NaverAdapterClass.instance()