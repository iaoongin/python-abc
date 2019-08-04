from advance.HttpRequest import HttpRequest
from advance.HttpServlet import HttpServlet
from advance.HttpResponse import HttpResponse
from advance.Logger import Logger

logger = Logger.get_logger("http servlet")


class HttpServletWrap(HttpServlet):
    """装饰器"""

    http_servlet: None

    def __init__(self, http_servlet):
        self.http_servlet = http_servlet

    def service(self, request, client_socket):
        self.http_servlet.service(request, client_socket)

    def do_put(self, request=HttpRequest, response=HttpResponse):
        """添加"""
        self.http_servlet.do_put(request, response)

    def do_post(self, request, response):
        """修改"""
        self.http_servlet.do_post(request, response)

    def do_delete(self, request, response):
        """删除"""
        self.http_servlet.do_delete(request, response)

    def do_get(self, request, client_socket):
        """查询"""
        self.http_servlet.do_get(request, client_socket)

    def writeFile(self, request, response):
        self.http_servlet.writeFile(request, response)
