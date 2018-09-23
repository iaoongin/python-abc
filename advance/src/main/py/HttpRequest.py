import HttpMethod

HttpMethod = HttpMethod.HttpMethod


class HttpRequest:
    """http请求"""

    '''请求方式'''
    method = ''
    '''请求资源地址'''
    request_uri = ''
    '''协议'''
    protocol = ''
    '''get url str'''
    url_param_str = ''

    content_type = ''

    content_length = 0

    request_body = ''

    @staticmethod
    def parse(recv):
        _http_requset = HttpRequest()
        splits = recv.splitlines(False)
        for i in range(len(splits)):
            temp = str(splits[i], 'utf8')
            if i == 0:
                split = temp.split(' ')

                # method
                _http_requset.method = split[0]
                # request_uri
                _http_requset.request_uri = split[1]

                # params
                if _http_requset.method in ('GET', 'get'):
                    sp = split[1].split('?')
                    # modify request_uri
                    _http_requset.request_uri = sp[0]
                    if len(sp) > 1:
                        _http_requset.url_param_str = sp[1]

            # body
            if _http_requset.method in (HttpMethod.PUT.value + HttpMethod.POST.value + HttpMethod.DELETE.value):
                if temp == '':
                    for j in range(i + 1, len(splits)):
                        _http_requset.request_body += str(splits[j], 'utf8')

            _http_requset.protocol = split[2]

        return _http_requset

    def __str__(self):
        return '{' \
               'method: %s,' \
               'request_uri: %s,' \
               'protocol: %s,' \
               'url_param_str: %s,' \
               'request_body: %s' \
               ' }' % \
               (self.method, self.request_uri, self.protocol, self.url_param_str, self.request_body)
