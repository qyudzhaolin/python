from selenium.webdriver.common.by import By

# login_url
URL = 'https://cliengage.org/'  # waitting for edit
LOGIN_BTN = [By.NAME, 'publicLogin']
UTHealth_Login = [By.LINK_TEXT, 'UTHealth Login']
UTHealth_Username = [By.ID, 'Ecom_User_ID']
Username = ['abc']  # waitting for edit
UTHealth_Password = [By.ID, 'Ecom_Password']
Password = ['def']  # waitting for edit
UTHealth_Login_btn = [By.ID, 'loginButton']


dashboard_url = 'home/Dashboard/sign-in'


Sign_In_With_Your_Google_Account = [By.LINK_TEXT, 'Sign In with your Google Account']
Google_email = [By.ID, 'identifierId']
Google_password = [By.NAME, 'password']
Google_Next = [By.CLASS_NAME, 'CwaK9']

