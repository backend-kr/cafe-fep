import logging

import requests as requests

from common.designpatterns import dotdict
from common.exceptions.base import PreconditionFailed

logger = logging.getLogger('django.server')

class APIResponse(dotdict):
    pass


class APIRequest:
    response_class = APIResponse

    def __init__(self, url, headers=None, body=None, **kwargs):
        if headers is None:
            headers = {
                'Content-Type': 'application/json'
            }

        if body is None:
            body = dict()

        self.url = url
        self.headers = headers
        self.body = body

    def update_headers(self, params):
        self.headers.update(params)

    def send(self, method='POST'):
        if method == 'GET':
            self.url = self.url.format(**self.body)
            # self.body = None

        response = requests.request(
            method, self.url,
            headers=self.headers,
            params=self.body
        )

        if not response:
            logger.error(
                'received the error response. %s %s %s %s\n%s' %
                (method, self.url, response.status_code, len(response.content), response.text))
            raise PreconditionFailed(f'The response is not successful. - {response.text}')
        return self.response_class(**response.json())


