from selenium.webdriver.common.by import By

# test logout
LOGOUT = [By.XPATH, '//a[@href="http://engage.sunnet.cli/home/LogOut"]']  # waiting for edit


# Class & Student Management
Class_Student_Management = [By.LINK_TEXT, 'Class & Student Management']
# Community/District search
txtCommunity = [By.ID, 'txtCommunity']
txtSchool = [By.ID, 'txtSchool']

Community_Name = 'CLI TEST COMMUNITY'  # waitting for edit
School_Name = 'Test School 1'  # waitting for edit

Community_Search_Btn = [By.CSS_SELECTOR, '.search-btn']

Features = [By.CSS_SELECTOR, '.feature-btn']

TRS = [By.XPATH, '//*[@id=\'Areas_Community_Views_Community_FeaturesCli\']/div[2]/div[1]/div[6]/input']

Features_Sub_Btn = [By.XPATH, '//*[@id=\'Areas_Community_Views_Community_FeaturesCli\']/div[8]/button[1]']

User_M = [By.XPATH, '//a[@href="/Invitation/Public/Dashboard"]']
TRS_Specialist = [By.LINK_TEXT, 'TRS Specialist']
First_Name = [By.ID, 'UserInfo_FirstName']
Last_Name = [By.ID, 'UserInfo_LastName']

Title_Role = [By.XPATH, '//*[@id="PositionId"]/option']
Address = [By.ID, 'Address']
State = [By.XPATH, '//*[@id="StateId"]/option']
County = [By.XPATH, '//*[@id="CountyId"]/option']

Primary_Phone_Number = [By.ID, 'UserInfo_PrimaryPhoneNumber']
Primary_Number_Type = [By.XPATH, '//*[@id="UserInfo_PrimaryNumberType"]/option']
Primary_Email = [By.ID, 'UserInfo_PrimaryEmailAddress']

Submit = [By.CSS_SELECTOR, '.submit-btn']


TRS_Class_M = [By.XPATH, '//a[@href="/TRSClass/TRSClass/index"]']
Add_btn = [By.CSS_SELECTOR, '.create-btn']

Class_Name = [By.ID, 'Name']

Assessor = [By.ID, 'TrsAssessorId']
Mentor = [By.ID, 'TrsMentorId']


AoC = [By.XPATH, '//*[@id="divAgeChildren"]/div/div[2]/div/table/tbody/tr']
check_AoC = [By.XPATH, '//*[@id="divAgeChildren"]/div/div[2]/div/table/tbody/tr[2]/td[1]/label']

AoC0m = [By.ID, 'chk11']
AoC18m = [By.ID, 'chk12']
AoC3y = [By.ID, 'chk13']
AoC5y = [By.ID, 'chk14']


School_Management = [By.LINK_TEXT, 'School Management']
School_txtSchool = [By.ID, 'SchoolName']
School_Search_Btn = [By.XPATH, '//*[@id="formSearch"]/div[3]/div[3]/button']
School_Edit = [By.CSS_SELECTOR, '.pencil-btn']





# TRS Assessment Tool
TRS_A_Tool = [By.CSS_SELECTOR, ".parent-dashboard-content-texas .list-2:nth-child(1) .list-content"]

TRS_A_Tool_Search_Btn = [By.CSS_SELECTOR, '.search-bg-btn']
TRS_A_Tool_Play_Btn = [By.CSS_SELECTOR, '.icon-play']
Event_Log = [By.LINK_TEXT, 'Event Log']

Create_Event_Btn = [By.LINK_TEXT, 'Create Event']
Date_Created = [By.ID, 'dateCreated0']
Created_By = [By.NAME, 'createdBy0']

Event_Type = [By.XPATH, '//*[@id="EventType0"]/option']
Event_Log_Save_Btn = [By.CSS_SELECTOR, '.save-btn']

Modified_Btn = [By.CSS_SELECTOR, "tr:nth-child(1) .icon-pencil"]


check_Notification = [By.XPATH, '//*[@class=\'table table-striped table-hover\']/tbody/tr/td[6]/input']

close_btn = [By.CSS_SELECTOR, ".close > span:nth-child(1)"]


edit_Star_Level_Change = [By.XPATH, '//*[@name="EventType"]/option[5]']

edit_Accreditations = [By.XPATH, '//*[@name="EventType"]/option[8]']

selected = [By.XPATH, '//*[@selected="selected"]']

approval_date = [By.ID, 'ApprovalDate']
recertification_date = [By.ID, 'RecertificationDate']

change_btn = [By.CSS_SELECTOR, '.btn-danger']
comment = [By.TAG_NAME, 'textarea']


edit_auto_assign = [By.XPATH, '//*[@name="EventType"]/option[8]']
accreditations_select = [By.XPATH, '//*[@id="Areas_Trs_Views_Index_Accreditations"]/div/div/div/label']
verified_star_designation = [By.XPATH, '//*[@id="verifiedStar"]/option']
