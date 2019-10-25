# coding:utf-8
# code by Loid

class Response(object):

    def __init__(self, request):
        self._code = request.status_code
        self._body = request.content
        self._headers = request.headers

    @property
    def body(self):
        return self._body

    @property
    def code(self):
        return self._code

    @property
    def headers(self):
        return self._headers

    @property
    def location(self):
        return self._headers.get("Location", None)

# from libs.Request import Request
#
# req = Request("http://www.pna.com.cn/index.asp?id=11&action=news").get()
# res = Response(req)
# print(res.code)