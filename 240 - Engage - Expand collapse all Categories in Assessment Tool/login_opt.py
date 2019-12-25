from selenium import webdriver
from config.ELEMENTS_LOGIN import *
from time import sleep

driver = None

# def login_admin():
#     global driver
#     if driver is None:
#         driver = webdriver.Chrome()
#         driver.maximize_window()
#         driver.implicitly_wait(10)
#         driver.get(URL)
#         driver.find_element(LOGIN_BTN[0], LOGIN_BTN[1]).click()
#         driver.find_element(UTHealth_Login[0], UTHealth_Login[1]).click()
#         driver.find_element(UTHealth_Username[0], UTHealth_Username[1]).send_keys(Username)
#         driver.find_element(UTHealth_Password[0], UTHealth_Password[1]).send_keys(Password)
#         driver.find_element(UTHealth_Login_btn[0], UTHealth_Login_btn[1]).click()
#         if driver.current_url == URL + dashboard_url:
#             print('Login Admin User successfully!')
#         else:
#             print('Login Admin User false!')
#
#     return driver
#
#
# def login_user(email, password):
#     driver.get(URL)
#     driver.find_element(LOGIN_BTN[0], LOGIN_BTN[1]).click()
#     driver.find_element(Sign_In_With_Your_Google_Account[0], Sign_In_With_Your_Google_Account[1]).click()
#     driver.find_element(Google_email[0], Google_email[1]).send_keys(email)
#     driver.find_element(Google_Next[0], Google_Next[1]).click()
#     driver.find_element(Google_password[0], Google_password[1]).send_keys(password)
#     sleep(3)
#     driver.find_element(Google_Next[0], Google_Next[1]).click()

########################################################################################################################

def login_admin():
    global driver
    if driver is None:
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get('http://engage.sunnet.cli/home/invite/1')
        driver.find_element_by_link_text('Login').click()

    return driver



def login_user(UserID):
    driver.get('http://engage.sunnet.cli/home/invite/%s' % UserID)
    driver.find_element_by_link_text('Login').click()
