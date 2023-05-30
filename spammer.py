import pyautogui
import time

# Check the size of your display
print(pyautogui.size())

# Delay for moving the moise pointer to the specified chat position
time.sleep(5)

# Main loop for the spam change n value for number of messages
n=100
pyautogui.click()
for i in range (n):
    pyautogui.typewrite('Message to be spammed')
    pyautogui.press('enter')
