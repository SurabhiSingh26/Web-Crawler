from selenium import webdriver
import requests
from bs4 import BeautifulSoup
search='messi Birthday'
google=''
google='https://www.google.co.in/search?dcr=0&source=hp&ei=klCkWsDPN4vevgTjjoKIDw&q='+search+'&oq=hi&gs_l=psy-ab.12...1163.1170.0.1244.2.1.0.0.0.0.0.0..0.0....0...1c..64.psy-ab..2.0.0....0.GU37eSgF-fQ'
print('Working')
driver = webdriver.Chrome(r'C:\Users\Surabhi Singh\Downloads\chromedriver.exe')
driver.get(google)
content = driver.find_element_by_class_name('_XWk')
print(content.get_attribute('innerHTML'))