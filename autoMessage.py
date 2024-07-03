import pyautogui as aut
import time
time.sleep(5)

animalList = open("animal.txt", "r")

for a in range(0 ,50):
    name = animalList.readline()
    aut.typewrite("Gaurav is " + name)
    time.sleep(.3)
    aut.press("Enter")



