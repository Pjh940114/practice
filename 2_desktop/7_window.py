import pyautogui

# fw = pyautogui.getActiveWindow() # 현재 활성화된 창 (VScode)
# print(fw.title) # 창의 제목 정보
# print(fw.size) # 창의 크기 정보 (width, height)
# print(fw.left, fw.top, fw.right, fw.bottom)
# pyautogui.click(fw.left + 25, fw.top + 20)

# for w in pyautogui.getAllWindows():
#     print(w)

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
print(w)
if w.isActive == False:
    w.activate() # 활성화 (맨 앞으로 가져오기)

if w.isMaximized == False:
    w.maximize() # 최대화

if w.isMinimized == False:
    w.minimize() # 최소화    

pyautogui.sleep(1)

w.restore() # 원복
w.close() #윈도우 닫기