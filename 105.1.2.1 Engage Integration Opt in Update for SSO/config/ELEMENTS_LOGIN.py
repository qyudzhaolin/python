from selenium.webdriver.common.by import By

# login_url
URL = 'http://engage.sunnet.ql/'  # 待改
TECPDS_URL = 'http://tecpds.qc/login/devlogin/'  # 待改
LOGIN_URL = 'home/invite/'
G_LOGIN_SU_URL = 'home/Dashboard/sign-in'

# login elements
LOGIN_EMAIL = [By.ID, 'txtEmail']
LOGIN_EMAIL_SUBMIT = [By.XPATH, '/html/body/input[2]']
G_TAG_LOGIN_PAGE = [By.XPATH, '/html/body/a[1]']

# TECPDS login elements
TRAINER_LOGIN = [By.ID, 'rtTrainer']
PRACTITIONER_LOGIN = [By.ID, 'rtPractioner']
CENTER_DIRECTOR_LOGIN = [By.ID, 'rtCD']
GOOGLEID_GMAIL = [By.ID, 'txtGoogleId']
GOOGLE_LOGIN = [By.ID, 'btnGoogleLogin']

# CLI URL
G_COMMUNITY_CLI_URL = 'http://engage.sunnet.ql/Community/Community/Index'
G_SCHOOL_CLI_URL = 'http://engage.sunnet.ql/School/School/index'