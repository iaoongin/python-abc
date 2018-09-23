import HttpRequest
from HttpMethod import HttpMethod
from HttpResponse import HttpResponse
from Logger import Logger
from advance.src.main import dirname


class Servlet:
    """处理请求和响应"""

    request = None
    response = None

    def service(self, request, response):
        self.request = request
        self.response = response


logger = Logger.get_logger("http servlet")


class HttpServlet(Servlet):

    def service(self, request, client_socket):
        method = request.method
        logger.info('请求方式: ' + method)
        logger.info('请求资源: ' + request.request_uri)
        if method in HttpMethod.POST.value:
            self.do_post(request, client_socket)
        elif method in HttpMethod.DELETE.value:
            self.do_delete(request, client_socket)
        elif method in HttpMethod.PUT.value:
            self.do_put(request, client_socket)
        else:  # get
            self.do_get(request, client_socket)

    def do_put(self, request=HttpRequest, response=HttpResponse):
        """添加"""
        pass

    def do_post(self, request, response):
        """修改"""
        pass

    def do_delete(self, request, response):
        """删除"""
        pass

    def do_get(self, request, client_socket):
        """查询"""
        request_uri = request.request_uri
        uri_suffix = request_uri[request_uri.rfind('.') + 1: len(request_uri)]
        if uri_suffix in ('ico', 'png', 'jpg', 'gif'):
            response = HttpResponse(client_socket, content_type='image/*')
            self.writeFile(request, response)
            response.close()
            return

        if request_uri == "/":
            response = HttpResponse(client_socket)
            response.write_string('你好')
            response.close()
            return

        if uri_suffix in ("html", 'xhtml'):
            response = HttpResponse(client_socket, content_type='text/html')
            self.writeFile(request, response)
            response.close()
            return

        response = HttpResponse(client_socket, status='404', reason='Not Found')
        response.write_string("404 Not Found")
        response.close()
        return

    def writeFile(self, request, response):
        with open(dirname + "/resources" + request.request_uri, 'rb') as file:
            bufl = 1024
            cont = file.read(bufl)
            while len(cont) > 0:
                response.write(cont)
                cont = file.read(bufl)
