from enum import Enum


class HttpMethod(Enum):
    """http请求方式"""
    PUT = ('put', "PUT")
    DELETE = ('delete', "DELETE")
    POST = ('post', "POST")
    GET = ('get', "GET")


# a = (HttpMethod.PUT.value + HttpMethod.POST.value + HttpMethod.DELETE.value)
