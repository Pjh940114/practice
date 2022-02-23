import pyautogui
import pyperclip
import sys

# 그림판 실행하기
pyautogui.hotkey("win", "r")
pyautogui.write("mspaint")
pyautogui.press("enter")

pyautogui.sleep(2)

# 그림판
w = pyautogui.getWindowsWithTitle("제목 없음 - 그림판")[0]
# if w.isMaximized == False:
#     w.maximize() # 최대화

# 글자 입력 아이콘 좌표 이동 후 클릭
pyautogui.click(590, 240)
# 흰 부분 선택
pyautogui.click(590, 440)

# 한글 입력 함수
def my_write(text):
    pyperclip.copy(text) # 글자를 클립보드에 저장
    pyautogui.hotkey("ctrl","v") # 클립보드에 있는 내용을 붙여넣기   
my_write("참 잘했어요")

# 1초 대기
pyautogui.sleep(1)

# 프로그램 종료
# pyautogui.hotkey("alt", "f4")
w.close()

# 저장안함
pyautogui.press("n")

# 이미지가 오류나서 좌표 지정해서 함