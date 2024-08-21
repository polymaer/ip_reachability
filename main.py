import requests
import json
from ping3 import ping
import time

def get_current_time_millis():
    return int(time.time() * 1000)

def get_ips_for_domain(domain, cookie):
    current_time = get_current_time_millis()
    url = f'https://ipchaxun.com/domain/read.do?domain={domain}&time={current_time}'
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': cookie,
        'Pragma': 'no-cache',
        'Referer': f'https://ipchaxun.com/{domain}/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data.get('ips', [])
    else:
        print(f"Failed to retrieve IPs for domain {domain}")
        return []

def check_reachability(ip):
    response = ping(ip)
    if response is not None:
        return True
    else:
        return False

def main(domain, cookie):
    ips = get_ips_for_domain(domain, cookie)
    if not ips:
        print(f"No IPs found for domain {domain}")
        return

    print(f"IPs found for domain {domain}: {ips}")
    for ip in ips:
        reachable = check_reachability(ip)
        status = "reachable" if reachable else "unreachable"
        print(f"IP {ip} is {status}")

domain = 'your domain'
cookie = 'your cookie' 
if __name__ == "__main__":
    domain = domain
    cookie = cookie
    main(domain, cookie)