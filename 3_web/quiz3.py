import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

# URL 접속
browser.get('https://www.w3schools.com/')

# 화면 중간 LEARN HTML 클릭
browser.find_element_by_xpath('//*[@id="main"]/div[2]/div/div[1]/a[1]').click()

# 화면 상단 HOW TO 클릭
browser.find_element_by_xpath('//*[@id="topnav"]/div/div/a[10]').click()

# 화면 상단 Contact Form 클릭
# 1. 메뉴가 추가 될 경우 번호가 달라질 수 있음
browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[117]').click()

# 2. Contact Form 이라는 2개 이상의 링크 텍스트가 있는 경우엔 실패
# browser.find_element_by_link_text('Contact Form').click() 

# 3. xpath 중 contact form 이라는 링크 텍스트를 찾음, 가장 좋은 방법
# browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[text()="Contact Form"]').click()

# 4. 일부 텍스트만 확인
# browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[contains(text(), "Contact"]').click()

# 입력란에 아래 값 입력
first_name = "나도"
last_name = "코딩"
country = "Canada"
subject = "퀴즈 완료하였습니다"

# First Name
browser.find_element_by_xpath('//*[@id="fname"]').send_keys(first_name)

# Last Name
browser.find_element_by_xpath('//*[@id="lname"]').send_keys(last_name)

# Country
browser.find_element_by_xpath(' //*[@id="country"]/option[text()="{}}"]'.format(country)).click()

# Subject
browser.find_element_by_xpath('//*[@id="main"]/div[3]/textarea').send_keys(subject)

time.sleep(5) # 5초 대기
browser.find_element_by_xpath('//*[@id="main"]/div[3]/a').click()

time.sleep(5) # 5초 대기
browser.quit()