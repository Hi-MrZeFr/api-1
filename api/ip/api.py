# IP工具类
class IpUtil:
    # X-Forwarded-For:简称XFF头，它代表客户端，也就是HTTP的请求端真实的IP，只有在通过了HTTP 代理或者负载均衡服务器时才会添加该项。
    @staticmethod
    def get_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]  # 多次反向代理后会有多个ip值，第一个ip才是真实ip
        else:
            ip = request.META.get('REMOTE_ADDR')  # 这里获得代理ip
        return ip
