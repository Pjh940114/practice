from attr import attrs
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # soup 객체에서 처음 발견되는 a element 출력 
# print(soup.a.attrs) # a element 속성 정보를 출력
# print(soup.a["href"]) # a element href '값' 정보를 출력

# print(soup.find("a", attrs={"class" : "Nbtn_upload"})) # class = "Nbtn_upload" 인 a element 를 찾음
# print(soup.find(attrs={"class" : "Nbtn_upload"})) # class = "Nbtn_upload" 인 어떤 element 를 찾음

# print(soup.find("li", attrs = {"class":"rank01"}))
rank1 = soup.find("li", attrs = {"class":"rank01"})
# print(rank1.a.get_text())
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.get_text())
# print(rank1.parent)
# rank2 = rank1.find_next_sibling("li")
# print(rank2.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.get_text())
# rank2 = rank3.find_previous_sibling("li")
# print(rank2.get_text())

# print(rank1.find_next_siblings("li"))

webtoon = soup.find("a", text="더 복서-더 복서 외전. 악연(3)")
print(webtoon)
