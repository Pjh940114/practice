import pyautogui
# 스크린 샷 찍기
# img = pyautogui.screenshot()
# img.save("screenshot.png") # 파일로 저장

#pyautogui.mouseInfo()
#652,131 18,18,18 #121212

pixel = pyautogui.pixel(652, 131)
print(pixel)

# print(pyautogui.pixelMatchesColor(652,131,(18,18,18)))
print(pyautogui.pixelMatchesColor(652,131,pixel))