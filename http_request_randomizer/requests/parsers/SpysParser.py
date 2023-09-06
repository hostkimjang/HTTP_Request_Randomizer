import logging
import pprint
import re
import bs4
import requests
import execjs
from bs4 import BeautifulSoup
from http_request_randomizer.requests.parsers.js.UnPacker import JsUnPacker
from http_request_randomizer.requests.parsers.UrlParser import UrlParser
from http_request_randomizer.requests.proxy.ProxyObject import ProxyObject, AnonymityLevel, Protocol

logger = logging.getLogger(__name__)
__author__ = 'kimjang'

"""
session = requests.Session()
session.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"})

resp = session.post("https://spys.one/en/https-ssl-proxy/")
soup = BeautifulSoup(resp.text, "html.parser")
sp = soup.select("tr:nth-child(1)")
xx0 = sp[2].select("input[type=hidden]")[0].attrs["value"]

payload = {
    'xx0': xx0,
    'xpp': '5',
    'xf1': '0',
    'xf4': '0',
    'xf5': '0'
}


url = "https://spys.one/en/https-ssl-proxy/"


def get_index():
	session = requests.Session()
	session.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"})

	resp = session.post("https://spys.one/en/https-ssl-proxy/")
	soup = BeautifulSoup(resp.text, "html.parser")
	sp = soup.select("tr:nth-child(1)")
	xx0 = sp[2].select("input[type=hidden]")[0].attrs["value"]

	payload = {
		'xx0': xx0,
		'xpp': '5',
		'xf1': '0',
		'xf4': '0',
		'xf5': '0'
	}

	try:
		rsp = session.post(url=url, data=payload)
		if rsp.status_code == 200:
			html = rsp.text
			return html
		else:
			exit('Can not get the website.')
	except ConnectionError:
		exit('Please run your proxy app and try again.')


def parse_proxy_info(html):
	pattern = re.compile('onmouseout.*?spy14>(.*?)<.*?>"(.*?)<\/.*?>([HTTPS|SOCKS5]+)', re.S)
	info = re.findall(pattern, html)
	if len(info) > 30:
		print('PROXY: {}'.format(len(info)))
	else:
		exit('Operation too frequent, please change your proxy and try again later.')
	if 'https-' in url:
		pattern_js = re.compile('\/javascript">(eval.*\)\))')
	else:
		pattern_js = re.compile('table><script.*?>(.*?)<\/script')
	ec = re.findall(pattern_js, html)
	if 'eval(' in ec[0]:
		with open('ejs.js', 'w+', encoding='utf8') as f:
			f.write(ec[0][5:-1])
		hc = execjs.eval(open('ejs.js', 'r', encoding='utf8').read())
		eec = hc.replace(';',';\n')
	else:
		eec = ec[0].replace(';', ';\n')
	ctx = 
	function port()
	{
	%s
	return port;
	}
    

	for i in info:
		ip = i[0]
		protocol = i[2].lower()
		a = i[1].replace('+(', '+String(').replace('))', ')')
		b = 'port = ' + a[1:]
		c = eec + b
		d = ctx % (str(c))
		port = execjs.compile(d).call('port')
		print(ip, port, protocol)

"""

#html = get_index()
#parse_proxy_info(html)


# Samair Proxy now renamed to: spys.one
url = "https://spys.one/en/https-ssl-proxy/"
class SpysProxyParser(UrlParser):
    def __init__(self, id, web_url, timeout=None):
        self.base_url = web_url
        self.web_url = web_url + "/list/"
        self.timeout = timeout
        self.id = id  # 추가: id 속성 설정

        UrlParser.__init__(self, id=id, web_url=web_url, timeout=timeout)

    def parse_proxyList(self):
        curr_proxy_list = []
        try:
            page_set = self.get_index()
            proxy_info_list = self.parse_proxy_info(page_set)

            for proxy_info in proxy_info_list:
                ip, port, protocol = proxy_info
                proxy_obj = self.create_proxy_object(ip, port)
                if proxy_obj is not None:
                    curr_proxy_list.append(proxy_obj)

        except Exception as e:
            print("Error:", str(e))

        return curr_proxy_list

    def get_index(self):
        session = requests.Session()
        session.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"})
        resp = session.post("https://spys.one/en/https-ssl-proxy/")
        soup = BeautifulSoup(resp.text, "html.parser")
        sp = soup.select("tr:nth-child(1)")
        xx0 = sp[2].select("input[type=hidden]")[0].attrs["value"]

        payload = {
            'xx0': xx0,
            'xpp': '1',
            'xf1': '0',
            'xf4': '0',
            'xf5': '0'
        }

        try:
            rsp = session.post(url=url, data=payload)
            if rsp.status_code == 200:
                html = rsp.text
                return html
            else:
                exit('Can not get the website.')
        except ConnectionError:
            exit('Please run your proxy app and try again.')

    def parse_proxy_info(self, html):
        curr_proxy_list = []
        pattern = re.compile('onmouseout.*?spy14>(.*?)<.*?>"(.*?)<\/.*?>([HTTPS|SOCKS5]+)', re.S)
        info = re.findall(pattern, html)
        if len(info) > 30:
            print('PROXY: {}'.format(len(info)))
        else:
            exit('Operation too frequent, please change your proxy and try again later.')
        if 'https-' in url:
            pattern_js = re.compile('\/javascript">(eval.*\)\))')
        else:
            pattern_js = re.compile('table><script.*?>(.*?)<\/script')
        ec = re.findall(pattern_js, html)
        if 'eval(' in ec[0]:
            with open('ejs.js', 'w+', encoding='utf8') as f:
                f.write(ec[0][5:-1])
            hc = execjs.eval(open('ejs.js', 'r', encoding='utf8').read())
            eec = hc.replace(';', ';\n')
        else:
            eec = ec[0].replace(';', ';\n')
        ctx ="""
        function
        port()
        {
        % s
        return port;
        }"""
        for i in info:
            ip = i[0]
            protocol = i[2].lower()
            a = i[1].replace('+(', '+String(').replace('))', ')')
            b = 'port = ' + a[1:]
            c = eec + b
            d = ctx % (str(c))
            port = execjs.compile(d).call('port')
            print(ip, port, protocol)
            curr_proxy_list.append((ip, port, protocol))
        pprint.pprint(curr_proxy_list)
        return curr_proxy_list

    def create_proxy_object(self, row, port):
        for td_row in row.findAll("td"):
            if td_row.attrs['data-label'] == 'IP:port ':
                text = td_row.text.strip()
                ip = text.split(":")[0]
                # Make sure it is a Valid IP
                if not UrlParser.valid_ip(ip):
                    logger.debug("IP with Invalid format: {}".format(ip))
                    return None
            elif td_row.attrs['data-label'] == 'Anonymity Type: ':
                anonymity = AnonymityLevel.get(td_row.text.strip())
            elif td_row.attrs['data-label'] == 'Country: ':
                country = td_row.text.strip()
            protocols = [Protocol.HTTP]
        return ProxyObject(source=self.id, ip=ip, port=port, anonymity_level=anonymity, country=country, protocols=protocols)

    def __str__(self):
        return "{0} parser of '{1}' with required bandwidth: '{2}' KBs" \
            .format(self.id, self.web_url, self.minimum_bandwidth_in_KBs)
