import urllib.request as request


class HttpClient:
    """请求"""

    @staticmethod
    def get(url, param, param_str=''):
        print(url)
        print(param)
        if param:
            param_str = '?'
            for key in param:
                print(key)
                print(param[key])
                param_str += (key + "=" + param[key] + "&")
            param_str = param_str[0:-1]

        response = request.urlopen(url + param_str)
        read = response.read()
        print(read)
        return read

    def post(self):
        pass


# HttpClient.get("http://www.baidu.com", {'key': "1"})
