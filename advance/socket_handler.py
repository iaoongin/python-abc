import threading
from advance.HttpRequest import HttpRequest
from advance.HttpServlet import HttpServlet
from advance.PassByServlet import PassByServlet


class socket_handler(threading.Thread):
    clientsocket: None
    addr: None

    def __init__(self, clientsocket, addr):
        threading.Thread.__init__(self)
        self.clientsocket = clientsocket
        self.addr = addr

    def run(self):
        recv = self.clientsocket.recv(1024)
        # logger.info(str(recv, 'utf8'))

        self.clientsocket.settimeout(1000)
        # 解析请求
        http_request = HttpRequest.parse(recv)

        # 处理请求，并响应
        http_servlet = HttpServlet()
        http_servlet.service(http_request, self.clientsocket)
