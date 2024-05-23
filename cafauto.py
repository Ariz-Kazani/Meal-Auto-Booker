import pyautogui as pag
from time import sleep
from random import randint 

def autoAppLyBreakfast():
    pag.moveTo(738, 1100)
    pag.scroll(-150)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.scroll(-300)
    sleep(0.05)
    pag.click()
    sleep(0.2)
    pag.scroll(-270)
    sleep(0.05)
    pag.click()
    sleep(0.2)
    pag.scroll(-210)
    sleep(0.05)
    pag.click()
    # x = randint(1, 2)
    x = 2
    if x == 1: # get dates
        pag.scroll(-340)
        sleep(0.05)
        pag.click()
    elif x == 2: # get fruit salad
        pag.scroll(-300)
        sleep(0.05)
        pag.click()
        sleep(0.05)
        pag.scroll(-40)
        sleep(0.05)

    pag.scroll(-215)
    sleep(0.05)
    pag.click()
    sleep(0.2)
    pag.scroll(-165)
    sleep(0.05)
    pag.click()

def autoApplyHelper():
    # x = randint(1, 2)
    x = 2
    if x == 1: 
        pag.scroll(-260)
        sleep(0.2)
        pag.click()
        sleep(0.2)
        pag.scroll(-90)
    else:
        pag.scroll(-350)
        sleep(0.2)
        pag.click()
        sleep(0.2)
    
    pag.scroll(-300)
    sleep(0.2)
    pag.click()
    sleep(0.1)
    pag.scroll(-240)
    pag.click()
    pag.scroll(-85)
    sleep(0.1)
    pag.scroll(-425)
    pag.click()
    sleep(0.1)
    x = randint(1, 3)
    x = 2
    if x == 1: # get granola bar
        pag.scroll(-300)
        sleep(0.1)
        pag.click()
        sleep(0.1)
        pag.scroll(-133)
        sleep(0.05)
    elif x == 2: # get dates
        pag.scroll(-250)
        sleep(0.1)
        pag.click()
        sleep(0.1)
        pag.scroll(-183)
        sleep(0.05)
    else: # Dates
        pag.scroll(-433)
        sleep(0.1)
        pag.click()
        sleep(0.1)
    
    x = randint(1, 2)
    if x == 1: # get orange
        pag.scroll(-250)
        sleep(0.1)
        pag.click()
        sleep(0.1)
        pag.scroll(-97)
        sleep(0.05)
    elif x == 2: #get apple
        pag.scroll(-300)
        sleep(0.1)
        pag.click()
        sleep(0.1)
        pag.scroll(-47)
        sleep(0.05)
    else: #get fruit cup
        pag.scroll(-347)
        pag.click()
        sleep(0.1)
    
    x = randint(1, 5)
    x = 3
    if x == 1:
        pag.scroll(-165)
        sleep(0.1)
        pag.click()
        sleep(0.1)
        pag.scroll(-225)
        sleep(0.05)
    elif x == 2:
        pag.scroll(-255)
        sleep(0.1)
        pag.click()
        sleep(0.1)
        pag.scroll(-165)
    elif x == 3:
        pag.scroll(-300)
        sleep(0.1)
        pag.click()
        sleep(0.1)
        pag.scroll(-90)
    elif x == 4:
        pag.scroll(-345)
        sleep(0.1)
        pag.click()
        sleep(0.1)
        pag.scroll(-45)
    elif x == 5:
        pag.scroll(-390)
        sleep(0.1)
        pag.click()
        sleep(0.1)

def autoApplyDinner():
    pag.moveTo(738, 1100)
    pag.scroll(-240)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.scroll(-165)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    autoApplyHelper()


def autoApplyLunch():
    pag.moveTo(738, 1100)
    pag.scroll(-195)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.scroll(-210)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    autoApplyHelper()

def autoApply(firstname, lastname, email, studentNum, phoneNum, month, day, year, type):
    pag.moveTo(400, 150) # move to search bar
    pag.click()
    pag.typewrite('https://dining.carleton.ca/boxed-meals/')
    pag.press('enter')
    sleep(2)
    pag.moveTo(800, 900) 
    sleep(2)
    pag.scroll(8360) # reset scroll up
    sleep(2)
    pag.scroll(-1360) # move to name
    sleep(1)
    pag.click()
    pag.click()
    pag.typewrite(firstname)
    sleep(0.1)
    pag.moveTo(2200, 900) 
    sleep(0.1)
    pag.click()
    pag.click()
    pag.typewrite(lastname)
    sleep(0.1)
    pag.moveTo(800, 1100)
    pag.scroll(-110)
    sleep(0.1)
    pag.click()
    pag.typewrite(studentNum)
    sleep(0.1)
    pag.scroll(-30)
    pag.scroll(-140)
    sleep(0.1)
    pag.click()
    pag.typewrite(phoneNum)
    sleep(0.1)
    pag.scroll(-140)
    sleep(0.1)
    pag.click()
    pag.typewrite(email)
    sleep(0.1)
    pag.scroll(-170)
    sleep(0.1)
    pag.click()
    pag.typewrite(day+'/'+month+'/'+year)
    pag.press('enter')

    if type == 1:
        autoAppLyBreakfast()
    elif type == 2:
        autoApplyLunch()
    elif type == 3:
        autoApplyDinner()

    pag.press('tab')
    pag.typewrite('Halal')
    pag.press('tab')
    pag.press('tab')
    pag.press('enter')
    sleep(0.1)
    pag.scroll(-300)
    sleep(1)

    try:
        test = pag.locateOnScreen('images\captcha.png', grayscale=True, confidence=0.8)
        pag.confirm(text='Captcha Found', title='Captcha', buttons=['OK'])
    except:
        print('No Captcha found')
    try:
        test = pag.locateOnScreen('images\submit.png', grayscale=True, confidence=0.8)
        pag.click(test)
    except:
        print('No image found')



    


if __name__ == '__main__':
    month = input('Enter Month: ')
    day = input('Enter Day: ')
    endDay = input('Enter End Day: ')
    type = input('Enter Type (1 for breakfast, 2 for lunch and 3 for dinner): ')
    fName = input('Enter First Name: ')
    lName = input('Enter Last Name: ')
    email = input('Enter Email: ')
    studentNum = input('Enter Student Number: ')
    phoneNum = input('Enter Phone Number: ')
    print('First Name: ' + fName + ' Last Name: ' + lName + ' Email: ' + email + ' Student Number: ' + studentNum + ' Phone Number: ' + phoneNum)
    print('starting, go to chrome tab')
    sleep(3)
    for i in range(int(day), int(endDay) + 1):
        autoApply(fName, lName, email, studentNum, phoneNum, month, str(i), '2024', int(type))
        sleep(5)
    pag.alert(text='All Bookings have been completed!', title='Done', button='OK')
