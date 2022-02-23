# 웹 스크래핑을 이용하여 나만의 비서
# [조건]
# 1. 네이버에서 오늘 서울의 날씨정보를 가져온다.
# 2. 헤드라인 뉴스 3건을 가져온다
# 3. IT 뉴스 3건을 가져온다
# 4. 해거스 어학원 홈페이지에서 오늘의 영어 회화 지문을 가져온다

import requests
from bs4 import BeautifulSoup

# 1. 네이버에서 오늘 서울의 날씨정보를 가져온다.

def create_soup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8"
    soup = create_soup(url)
    
    # 어제보다 ~
    cast = soup.find("p", attrs = {"class" : "summary"}).get_text()
    # 현재 온도
    curr_temp = soup.find("strong", attrs={"class":"blind"}).get_text()
    # 최저 온도
    min_temp = soup.find("span", attrs={"class":"lowest"}).get_text()
    # 최고 온도
    max_temp = soup.find("span", attrs={"class":"highest"}).get_text()
    # 강수확률
    morning_rainfall = soup.find("span", attrs={"class":"rainfall"}).get_text().strip()
    afternoon_rainfall = soup.find("span", attrs={"class":"rainfall"}).get_text().strip()
    #미세먼지
    dust = soup.find("ul", attrs={"class": "today_chart_list"})
    pm10 = dust.find_all("li")[0].get_text().strip() #미세먼지
    pm25 = dust.find_all("li")[1].get_text().strip() #초미세먼지

    # 출력
    print(cast)
    print("현재 {} (최저 {} / 최고 {}".format(curr_temp, min_temp, max_temp))
    print("오전 {} / 오후{}".format(morning_rainfall, afternoon_rainfall))
    print(pm10 , pm25)
    
# 2. 헤드라인 뉴스 3건을 가져온다
def scrape_headline_news():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com/"
    soup = create_soup(url)
    hdnews = soup.find("div", attrs={"class": "cjs_news_tw"}).find_all("div")
    hdnews_01 = hdnews.find_all("div")[0].get_text().strip() # 1번 뉴스
    hdnews_02 = hdnews.find_all("div")[1].get_text().strip() # 2번 뉴스
    print(hdnews_01)

# 3. IT 뉴스 3건을 가져온다


# 4. 해거스 어학원 홈페이지에서 오늘의 영어 회화 지문을 가져온다

if __name__ == "__main__":
    # scrape_weather()
    scrape_headline_news()
