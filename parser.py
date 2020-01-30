import requests
import time
from bs4 import BeautifulSoup as bs

headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
}

base_url = 'https://jobs.tut.by/search/vacancy?search_period=30&area=1002&currency_code=BYR&text=python'



def testlog():
    print('Test started.')
    for x in range(1000000):
        x += 1
    print('Result:', '{}'.format(x))
    print('Test ended.')


def start_with_benchmark(func):
    start_time = time.time()
    func()
    print("--- %s seconds ---" % (time.time() - start_time))


def hh_parse(base_url, headers):
    jobs = []
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        divs = soup.find_all('div', attrs={'data-qa': 'vacancy-serp__vacancy'})
        for div in divs:
            title = div.find('a', attrs={'data-qa' : 'vacancy-serp__vacancy-title'}).text
            hrefs = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'})['href']
            topic1 = div.find('div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_responsibility'}).text
            topic2 = div.find('div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_requirement'}).text
            content = topic1 + topic2
            jobs.append({
                'title': title,
                'href': hrefs,
                'content': content
            })
        print(jobs)
    else:
        print('ERROR!')

hh_parse(base_url,headers)
