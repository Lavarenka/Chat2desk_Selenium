import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from login_pass import *

with webdriver.Chrome() as browser:
    browser.get('https://web.chat2desk.com/chat/')
    browser.maximize_window()
    time.sleep(1) #пауза 1 сек
    browser.find_element(By.CLASS_NAME, 'login-email').send_keys(my_login) # вводим логин
    time.sleep(1)
    browser.find_element(By.CLASS_NAME, 'login-password').send_keys(my_pass) # вводим пароль
    time.sleep(1)
    browser.find_element(By.CLASS_NAME, 'js-login-submit').click() # клацаем кнопку формы
    time.sleep(3)
    browser.get('https://web.chat2desk.com/chat/my?dialogID') # переходим по ссылке чатов

    time.sleep(10)
    # browser.find_element(By.ID, 'macros-icon-wrapper').click()
    # time.sleep(5)
    # browser.find_element(By.XPATH, '//div[@id="macroses-drop-down"]/div[3]')
    chat_items = browser.find_elements(By.CLASS_NAME, 'left-messages-container') # переходим на чаты

    count = 0 # счетчик

    def f(chat, count=0):
        for i in chat:
            try:
                i.click()
                time.sleep(1)
                browser.find_element(By.ID, 'macros-icon-wrapper').click()
                time.sleep(1)
                browser.find_element(By.ID, 'macros-icon-wrapper').click()
                time.sleep(5)
                count += 1
                if count == 5:
                    browser.get('https://web.chat2desk.com/chat/my?dialogID')
                    time.sleep(5)
                    chat_items = browser.find_elements(By.CLASS_NAME, 'left-messages-container')
                    return f(chat_items, count=0) # рекурсия
            except:
                time.sleep(1)
                print('не удачная попытка')
                continue


    f(chat_items)
