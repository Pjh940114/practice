import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 지정 폴더로 다운로드
chrome_options= Options()
chrome_options.add_experimental_option('prefs', {'download.default_directory':r'C:\pythonstudy\doit'})

browser = webdriver.Chrome(options=chrome_options)
browser.maximize_window() # 창 최대화

browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download')

browser.switch_to.frame('iframeResult') # frame 전환

# download 링크 클릭
elem = browser.find_element_by_xpath('/html/body/p[2]/a/img')
elem.click()

time.sleep(5) # 5초 대기
browser.quit()
