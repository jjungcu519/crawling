import csv
import requests
import pandas as pd
import time
from pprint import pprint
from bs4 import BeautifulSoup

results = []

for page in range(1, 101):

    URL = f'https://search.daum.net/search?w=news&nil_search=btn&DA=STC&enc=utf8&cluster=y&cluster_page=1&q=%EC%A0%84%EA%B8%B0%EC%B0%A8&sd=20240101000000&ed=20240731235959&period=u&p={page}'
    
    res = requests.get(URL)
    soup = BeautifulSoup(res.text, 'html.parser')


    presses = soup.select('div.area_tit > div > a > strong > span')
    headlines = soup.select('div.item-bundle-mid > div.item-title > strong > a')
    
    # for press in presses:
    #     print(press.text)

    # for headline in headlines:
    #     print(headline.text)

    # print('=============================')



# 데이터를 파일에 저장 (예시로 CSV 파일 모두 생성)
    for press, headline in zip(presses, headlines):
        results.append({"press": press.text.strip(), "headline": headline.text.strip()})


# 데이터프레임으로 변환
news_data = pd.DataFrame(results)

# CSV 파일로 저장
news_data.to_csv('news_data_2024.csv', index=False)