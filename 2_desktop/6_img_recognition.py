import pyautogui
# file_menu = pyautogui.locateOnScreen("file_menu.png")
# print(file_menu)

for i in pyautogui.locateAllOnScreen("checkbox.png"):
    print(i)
    pyautogui.click(i, duration=0.25)