import bs4
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy

if __name__ == '__main__':

    soup = bs4.BeautifulSoup
    proxies = RequestProxy().get_proxy_list()

    for proxy in proxies:
        print(proxy.get_address())

