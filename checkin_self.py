import requests
from bs4 import BeautifulSoup

def getCookies():
    url = 'https://panel0.serv00.com/login/'

    headers = {
        'authority': 'panel0.serv00.com',
        'origin': 'https://panel0.serv00.com',
        'referer': 'https://panel0.serv00.com/login/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203',

    }

    cookies = {
        'csrftoken': 'Jpc2Wlc7hCfAVtTHdxisDfZoKBgRSyOXDZ4F7ICLIELZKQ7bxxU1fsrF3OYHmHWO',
    }

    data = {
        'csrfmiddlewaretoken': 'MTQw0OFgfT2FdhzbtVl3ee3JMJp9P0XFGtI9bb5UGVy42ENFNVXCQrv05W7Zj95w',
        'username': 'wuxin',
        'password': '123456_qzpm@XL',
    }

    response = requests.post(url=url, headers=headers, cookies=cookies, data=data)
    # print(response)
    # print(response.cookies.items()[0])
    cookies = {i:j for i, j in response.cookies.items()}
    print(cookies)
    return cookies


def checkin(cookies):
    url = 'https://panel0.serv00.com/dashboard'

    headers = {
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'authority': 'panel0.serv00.com',
        'Referer': 'https://panel0.serv00.com/',
        'origin': 'hhttps://panel0.serv00.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188'
    }

    # cookies = {
    #     'csrftoken': 'ZtrKSpKeVJq96PrBwhYN1LUgg8SG5MuNRZPOebhTTu8VSAhg7CwPa35ofINEcLef',
    #     'sessionid': 'mvpu9pbflyh6ln43z2j8q5fes4nqj8pk'
    # }

    response = requests.get(url, headers=headers, cookies=cookies).text

    soup = BeautifulSoup(response, 'html.parser')
    text = soup.find_all('td')
    return text[5].text

if __name__ == '__main__':
    cookies = getCookies()
    print(checkin(cookies))