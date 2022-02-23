import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

browser.get('https://flight.naver.com/')

# 가는 날 클릭
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()
time.sleep(2)
browser.find_elements_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[4]/td[2]/button/b')[0].click()

# 오는 날
time.sleep(2)
browser.find_elements_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[2]/button/b')[0].click()

# 도착 클릭
time.sleep(2)
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]').click()

# 일본 클릭
time.sleep(2)
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/button[2]').click()

# 도쿄 클릭
time.sleep(2)
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/div/button[2]/i[1]').click()

# 항공권 검색 클릭
time.sleep(2)
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/button/span').click()

try: # element 값이 나올때 까지 10초 동안 기다린다.
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="__next"]/div/div[1]/div[4]/div/div[3]/div[1]/div')))
    print(elem.text)
except:
    print("실패했어요")

# 첫 번째 결과 출력
# elem = browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div[3]/div[1]/div')
# print(elem.text)

time.sleep(5) # 5초 대기
# browser.quit()
