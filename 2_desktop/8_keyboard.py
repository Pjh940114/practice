import pyautogui
w = pyautogui.getWindowsWithTitle("제목 없음")[0] # 메모장 1개 띄운 상태에서 가져옴
w.activate()

# pyautogui.write("12345")
# pyautogui.write("NadoCoding", interval=0.25)
# pyautogui.write("나도코딩")

# pyautogui.write(["t","e","s","t","left","left","right","l","a","enter"], interval=0.25)
# t e s t 순서대로 적고 왼쪽 방향키 2 번 오른쪽 방향키 1 번 l a 입력 후 엔터

# 특수 문자
# shift 4 -> $
# pyautogui.keyDown("shift") # shift 키를 누른 상태에서
# pyautogui.press("4") # 숫자 4를 입력하고
# pyautogui.keyUp("shift") # shift 키를 뗀다

# 조합키  (Hot Key)
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a") # press "a"
# pyautogui.keyUp("ctrl") # ctrl + a

# 간편한 조합키
# pyautogui.hotkey("ctrl", "alt", "shift", "a")
# # Ctrl > Alt > Shift > A > A 떼고 > Shift 떼고 > Alt 떼고 > Ctrl 떼고

# pyautogui.hotkey("ctrl", "a")

# 한글 입력
import pyperclip
# pyperclip.copy("나도 코딩") # "나도코딩" 글자를 클립보드에 저장
# pyautogui.hotkey("ctrl","v") # 클립보드에 있는 내용을 붙여넣기

#함수화
def my_write(text):
    pyperclip.copy(text) # "나도코딩" 글자를 클립보드에 저장
    pyautogui.hotkey("ctrl","v") # 클립보드에 있는 내용을 붙여넣기
    
my_write("나도코딩")

# win : ctrl + alt + del (자동화 종료)
