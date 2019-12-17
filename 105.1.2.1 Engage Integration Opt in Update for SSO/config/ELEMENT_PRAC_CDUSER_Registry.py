from selenium.webdriver.common.by import By

# Practitioner/Center Director 注册页面
Prac_CD_Birth_Date = [By.ID, 'BirthDate']
Prac_CD_Home_Address = [By.ID, 'HomeMailingAddress']
Prac_CD_City = [By.ID, 'City']
Prac_CD_Zip_Code = [By.ID, 'ZipCode']
Prac_CD_States = [By.ID, 'State']
Prac_CD_States_Select = [By.XPATH, "//*[@id='State']/selected='selected'"] # //*[@id="State"]/option[48]
Prac_CD_County = [By.ID, 'County']
Prac_CD_Primary_Phone_Number = [By.ID, 'PrimaryPhoneNumber']
Prac_CD_Primary_Number_Type = [By.ID, 'PrimaryNumberType']
Prac_CD_Submit_Button = [By.ID, 'btnSubmit']
