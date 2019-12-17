from selenium.webdriver.common.by import By

# 导航元素
Logout_Link = [By.XPATH, "/html/body/div[3]/div[1]/a[3]"]
My_Profile = [By.LINK_TEXT, "MY PROFILE"]

# Optin 弹窗元素
Opt_Do_WorkInTexas_No = [By.CSS_SELECTOR, ".checkbox:nth-child(2) #IsWorkInTexas"]
# /html/body/div[8]/div/div/form/div/div/div/div[2]/div/div[2]/div/div[2]/label/text()
# /html/body/div[8]/div/div/form/div/div/div/div[2]/div/div[2]/div/div[1]/label/text()
Opt_Do_WorkInTexas_Yes = [By.ID, "IsWorkInTexas"]
Opt_Do_WorkInEarly_No = [By.CSS_SELECTOR, ".checkbox:nth-child(2) #IsWorkInEarlyChildhoodDevelopment"]
Opt_Do_WorkInEarly_Yes = [By.ID, "IsWorkInEarlyChildhoodDevelopment"]
Opt_Save_Change_Button = [By.XPATH, '//*[@id="myModal"]/div/div/div[3]/button[1]']
Opt_Save_Change_Button_01 = [By.XPATH, "//*[@id='myModal1']/div/div/div[3]/button[1]"]
Opt_Role = [By.ID, "Role"]
Opt_Role_selects = [By.XPATH, "//*[@id='Role']/option"]  # //*[@id="Role"]/option[3]
Opt_AgeGroup = [By.ID, "AgeGroup"]
Opt_AgeGroup_selects = [By.XPATH, "//*[@id='AgeGroup']/option"]
Opt_Facility = [By.ID, "FacilityType"]
Opt_Facility_selects = [By.XPATH, "//*[@id='FacilityType']/option"]

# Optin 第二个弹窗元素
Opt_Yes_To_TECPDS = [By.ID, "IsParticipate"]
Opt_No_To_TECPDS = [By.CSS_SELECTOR, ".checkbox:nth-child(2) #IsParticipate"]
