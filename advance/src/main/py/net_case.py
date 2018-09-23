import socket
from socket_handler import socket_handler

from Logger import Logger


# 日志
logger = Logger.get_logger("net_case")


class Server:
    """网络服务"""
    # host = socket.gethostname()
    host = '127.0.0.1'
    port = 80
    serverSocket = None
    maxListenerNum = 5

    def __init__(self, port=80, max_listener_num=5):
        self.port = port
        self.maxListenerNum = max_listener_num

    def server(self):
        """开启服务"""

        self.serverSocket = socket.socket()
        self.serverSocket.bind((self.host, self.port))
        self.serverSocket.listen(self.maxListenerNum)

        logger.info("服务地址: %s:%s", self.host, self.port)

        while True:
            # 建立客户端连接
            clientsocket, addr = self.serverSocket.accept()
            # logger.info("连接地址: %s", addr)

            sh = socket_handler(clientsocket, addr);
            sh.start()

            # 过滤器
            # fileter = HttpFilter(http_request, http_response)
            # print(http_request.request_body)


# class Request:


server = Server(8888)
server.server()
