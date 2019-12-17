from selenium.webdriver.common.by import By

# login_url
URL = 'http://engage.sunnet.cli/'  # waitting for edit
LOGIN_URL = 'home/invite/'
G_LOGIN_SU_URL = 'home/Dashboard/sign-in'

# login elements
LOGIN_EMAIL = [By.ID, 'txtEmail']
LOGIN_EMAIL_SUBMIT = [By.XPATH, '/html/body/input[2]']
G_TAG_LOGIN_PAGE = [By.LINK_TEXT, "Login"]