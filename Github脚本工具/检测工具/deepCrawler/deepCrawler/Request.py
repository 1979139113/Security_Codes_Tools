# coding:utf-8
# code by Loid
import requests
import uuid

class Request(object):

    def __init__(self, url, method="GET", data=None, cookie=None, headers=None, timeout=10, **kwargs):
        self.url = url
        self._method = method.upper()
        self._data = data
        self._cookie = cookie
        self._headers = headers
        self._timeout = timeout
        try:
            self._uid = uuid.uuid3(uuid.NAMESPACE_URL, url)
        except UnicodeDecodeError as e:
            self._uid = "Not_uuid"

    def get_method(self):
        return self._method

    def get_data(self):
        return self._data

    def get_cookie(self):
        return self._cookie

    def get_headers(self):
        return self._headers

    def get_uuid(self):
        return self._uid

    def get(self):
        if self._method == "GET":
            return requests.get(self.url, cookies=self._cookie, headers=self._headers, timeout=self._timeout)

    def post(self):
        if self._method == "POST" and self._data:
            return requests.get(self.url, data=self._data, cookies=self._cookie, headers=self._headers, timeout=self._timeout)

