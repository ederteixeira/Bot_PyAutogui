import pyautogui
import time

pyautogui.PAUSE = 3

pyautogui.press("win")
pyautogui.write("Microsoft Teams")
pyautogui.press("enter")
pyautogui.PAUSE = 15
pyautogui.click(x=511, y=324)
pyautogui.PAUSE = 5
pyautogui.write("billgates@outlook.com")
pyautogui.click(x=800, y=454)
pyautogui.click(x=567, y=387)
pyautogui.write("micro$oft")
pyautogui.click(x=815, y=511)