import pyautogui

# sending 100 texts to a person on whatsapp in one shot.

# finding the coordinates of the chrome
# Just bring your cursor over the chrome icon and get the position in the form of coordinates
# x,y = pyautogui.position()
# print(x,y)

# to move our cursor over chrome in an automated way we pass the coordinates of that point to the moveTo function
# duration  basically defines the speed of the movement of the cursor. Here it is 2 seconds
pyautogui.moveTo(1064,1036, duration=2)
pyautogui.click()

# doing the same with the whatsapp text box. finding it's coordinates and then passing them to  moveTo function
pyautogui.moveTo(631,982,duration=2)
pyautogui.click()

# applying a for loop with i in range 100 as we wish to send the same text 100 times
for i in range(100):
    pyautogui.typewrite('cool_stuff using pyautogui')
    pyautogui.hotkey('enter')
    pyautogui.sleep(0.5)

# end of code
