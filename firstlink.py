import requests
from bs4 import BeautifulSoup
import time

def continue_crawl(search_history, target_url):
    response = requests.get(search_history[-1])
    data = response.text
    soup = BeautifulSoup(data)
    content_div = soup.find(id='mw-content-text').find(class_='mw-parser-output')
    for element in content_div.find_all("p", recursive=False):
        if element.find("a", recursive=False):
            first_relative_link = 'https://en.wikipedia.org'+str(element.find("a", recursive=False).get('href'))
            break
    try:
        b = search_history.index(first_relative_link)
    except ValueError:
        search_history.append(first_relative_link)
        print(first_relative_link)
        time.sleep(0.1)
        if(first_relative_link==target_url):
            return 1
        return 0
    else:
        print("cycle detected")
        return 1


search_history = ['https://en.wikipedia.org/wiki/Floating_point']
target_url = 'https://en.wikipedia.org/wiki/Philosophy'
count = 0;
while count < 25:
    found=continue_crawl(search_history , target_url)
    count = count + 1
    if found==1:
        break
print(search_history)
