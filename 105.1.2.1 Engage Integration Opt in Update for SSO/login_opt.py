from selenium import webdriver
from config.ELEMENTS_LOGIN import *
from time import sleep

driver = None

def two_types_login(UserID):
    try:
        driver.find_element(LOGIN_EMAIL[0], LOGIN_EMAIL[1]).send_keys(UserID)
        driver.find_element(LOGIN_EMAIL_SUBMIT[0], LOGIN_EMAIL_SUBMIT[1]).click()
    except:
        driver.find_element(G_TAG_LOGIN_PAGE[0], G_TAG_LOGIN_PAGE[1]).click()
    if driver.current_url == URL + G_LOGIN_SU_URL:
        print("Login (User ID: %s) successfully!" % UserID)
    else:
        print("Login (User ID: %s) unsuccessfully!" % UserID)


def login_admin(UserID):
    global driver
    if driver is None:
        print("Will login (User ID: %s)" % UserID)
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(URL + LOGIN_URL + UserID)
        sleep(2)
        two_types_login(UserID)

    return driver


def login_user(UserID):
    global driver
    driver.get(URL + LOGIN_URL + UserID)
    sleep(2)
    two_types_login(UserID)
    return driver

def teacpds_login(UserID):
    global driver
    driver.get(TECPDS_URL)
    sleep(2)
    driver.find_element(PRACTITIONER_LOGIN[0], PRACTITIONER_LOGIN[1]).click()
    driver.find_element(GOOGLEID_GMAIL[0], GOOGLEID_GMAIL[1]).send_keys(UserID)
    driver.find_element(GOOGLE_LOGIN[0], GOOGLE_LOGIN[1]).click()
    return driver

def tecpds_cduser_login(UserID):
    global driver
    driver.get(TECPDS_URL)
    sleep(2)
    driver.find_element(CENTER_DIRECTOR_LOGIN[0], CENTER_DIRECTOR_LOGIN[1]).click()
    driver.find_element(GOOGLEID_GMAIL[0], GOOGLEID_GMAIL[1]).send_keys(UserID)
    driver.find_element(GOOGLE_LOGIN[0], GOOGLE_LOGIN[1]).click()
    return driver