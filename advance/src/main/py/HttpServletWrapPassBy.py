import HttpRequest
from HttpServletWrap import HttpServletWrap
from HttpResponse import HttpResponse
from Logger import Logger

logger = Logger.get_logger("http servlet")


class HttpServletWrapPassBy(HttpServletWrap):
    """装饰器"""

    http_servlet: None

    def __init__(self, http_servlet):
        self.http_servlet = http_servlet

    def do_get(self, request, client_socket):
        """查询"""
        self.http_servlet.do_get(request, client_socket)

    def writeFile(self, request, response):
        self.http_servlet.writeFile(request, response)
