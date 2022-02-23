import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

browser.get('https://www.w3schools.com/html/')

time.sleep(5) # 5초 대기

# 특정 영역 스크롤
elem = browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[61]')

# 방법 1 : ActionChain
# from selenium.webdriver.common.action_chains import ActionChains
# actions = ActionChains(browser)
# actions.move_to_element(elem).perform()

# 방법 2 : 좌표 정보 이용
# xy = elem.location_once_scrolled_into_view # 함수가 아니니까 () 안씀
# print("type : ", type(xy)) # dict
# print("value : ", xy)

elem.click() # 스크롤 하지 않아도 클릭은 가능

time.sleep(5)
browser.quit()