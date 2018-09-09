class HttpFilter:
    """过滤器"""

    def __init__(self):
        return self

    def doFilter(self, chain, request, response):
        """过滤器"""
        chain.doFilter(request, response)
