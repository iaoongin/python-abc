import time


class HttpResponse:
    """http响应"""

    '''状态码'''
    code = 200

    '''响应类型'''
    content_type = ''

    content_length = 0

    '''响应体'''
    request_body = ''

    client_socket = None

    def __init__(self, client_socket, content_type='text/plain',
                 status='200', reason='OK', charset='utf8'):
        self.client_socket = client_socket
        self.write_string("HTTP/1.1 " + status + " " + reason)
        self.write_string('Content-Type: ' + content_type + ";charset=" + charset)
        self.write_string("")

    def write(self, cont):
        self.client_socket.send(cont)

    def write_string(self, msg):
        self.client_socket.send(bytes(msg + "\n", 'utf-8'))

    def flush(self):
        self.write_string("Date: " + time.strftime("%a, %b %d %H:%M:%S %Y GMT", time.localtime()))

    def close(self):
        self.client_socket.close()
