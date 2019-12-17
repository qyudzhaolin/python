from selenium.webdriver.common.by import By

# test logout
LOGOUT = [By.XPATH, '//a[@href="http://engage.sunnet.ql/home/LogOut"]']


# Class & Student Management
Mainsite_Url = "http://engage.sunnet.ql/Community/Community/Index"
Class_Student_Management = [By.LINK_TEXT, 'Class & Student Management']
# Community/District search
txtCommunity = [By.ID, 'txtCommunity']
txtSchool = [By.ID, 'txtSchool']

Community_Name = 'CLI TEST COMMUNITY'  # 待改
School_Name = 'Test School 1'  # 待改

Community_Search_Btn = [By.XPATH, '//*[@id="formSearch"]/div[2]/div[3]/button']

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









# community management elements

# Basic Information
ADD = (By.XPATH, '/html/body/div[4]/div[2]/div/div[1]/button')

# 判断Web Address提示语
WebAddress = [By.ID, 'WebAddress']
# 判断必填选项
RequiredName = [By.ID, 'BasicCommunityId-error']
RequiredType = [By.ID, 'FundingId-error']
# 超长字符输入
WebAddress_E = [By.ID, 'WebAddress-error']
DN_E = [By.ID, 'DistrictNumber-error']
CT_E = [By.ID, 'CommunityType-error']
CLEVER_T_E = [By.ID, 'Clever-error']
PA1_E = [By.ID, 'PhysicalAddress1-error']
PA2_E = [By.ID, 'PhysicalAddress2-error']
CITY_E = [By.ID, 'City-error']
PName_E = [By.ID, 'PrimaryName-error']
PE_E = [By.ID, 'PrimaryEmail-error']
SName_E = [By.ID, 'SecondaryName-error']
SE_E = [By.ID, 'SecondaryEmail-error']
Notes_E = [By.ID, 'Notes-error']

NAME = [By.ID, 'txtBasicCommunity']
NAMER = [By.XPATH, '//*[@id="txtBasicCommunity_dl"]/li']
# ID = [By.ID, 'Status']
ID_STATUS_AC = [By.XPATH, '//*[@id="Status"]/option[1]']
ID_STATUS_INAC = [By.XPATH, '//*[@id="Status"]/option[2]']
Type = [By.XPATH, '//select[@id=\'FundingId\']/option']
Type_1 = [By.XPATH, '//*[@id="FundingId"]/option[1]']  # Type (Funded by) 已改成随机选择
MOU_STATUS_S = [By.ID, 'statusSigned']
MOU_D = [By.XPATH, '//*[@id="divMouDocument"]/div[2]/div/div[2]/input']
MOU_D_R = [By.XPATH, '//*[@id="divMouDocument"]/div/div/span[3]/a']
MOU_STATUS_NS = [By.ID, 'statusNotSigned']
WA = [By.ID, 'WebAddress']
MOU_L = [By.XPATH, '//*[@id="divLogoUrl"]/div[2]/div/div[2]/input']
MOU_L_R = [By.XPATH, '//*[@id="divLogoUrl"]/div/div/span[3]/a']
DN = [By.ID, 'DistrictNumber']  # 选好社区后自动带出
CT = [By.ID, 'CommunityType']  # 没有字符长度限制提示
GOOGLE = [By.ID, 'AccessType1']
CLEVER = [By.ID, 'AccessType2']
CLEVER_T = [By.ID, 'SSOCommunityID']

# Community / District Physical Address(No P.O.Boxes)
PA1 = [By.ID, 'PhysicalAddress1']
PA2 = [By.ID, 'PhysicalAddress2']
CITY = [By.ID, 'City']
STATE = [By.XPATH, '//*[@id="StateId"]/option[45]']
COUNTY = [By.XPATH, '//*[@id="CountyId"]/option[102]']
ZIP = [By.ID, 'Zip']
PNumber = [By.ID, 'PhoneNumber']
# PNumber_E = [By.XPATH, '/html/body/div[4]/div[2]/div/form/div[3]/fieldset/div/div[4]/div[1]/span/span']
PN_HN = [By.XPATH, '//*[@id="PhoneNumberType"]/option[2]']

# Community/District Primary Contact
PS = [By.XPATH, '//select[@id=\'PrimarySalutation\']/option']
PT = [By.XPATH, '//select[@id=\'PrimaryTitleId\']/option']
PName = [By.ID, 'PrimaryName']
PE = [By.ID, 'PrimaryEmail']
PP = [By.ID, 'PrimaryPhone']
PPT = [By.XPATH, '//select[@id=\'PrimaryPhoneType\']/option']

# Community/District Secondary Contact
SS = [By.XPATH, '//select[@id=\'SecondarySalutation\']/option']
ST = [By.XPATH, '//select[@id=\'SecondaryTitleId\']/option']
SName = [By.ID, 'SecondaryName']
SE = [By.ID, 'SecondaryEmail']
SP = [By.ID, 'SecondaryPhone']
SPT = [By.XPATH, '//select[@id=\'SecondaryPhoneType\']/option']

# Community/District Notes
Notes = [By.ID, 'Notes']

# Others
# Submit = [By.ID, 'btnSubmit']
Cancel = [By.XPATH, '//*[@id="frmCommunity"]/div[8]/button[2]']
BM = [By.LINK_TEXT, 'Back to Community/District List']


# TCA = [By.CLASS_NAME, 'active']
TCR = [By.XPATH, '//*[@id="txtCommunity_dl"]/li']
SAll = [By.XPATH, '//*[@id="Status"]/option[1]']
SActive = [By.XPATH, '//*[@id="Status"]/option[2]']
SInactive = [By.XPATH, '//*[@id="Status"]/option[3]']
FAll = [By.XPATH, '//*[@id="FundingName"]/option[1]']
FD = [By.XPATH, '//*[@id="FundingName"]/option']

Result = [By.XPATH, '//*[@class="content-body-tab"]/table/tbody[1]/tr[1]/td[1]']
FN = [By.XPATH, '//*[@class="content-body-tab"]/table/tbody[1]/tr[1]/td[1]']

# Community/District List
DPP2 = [By.XPATH, '//*[@id="list_Community_ddlDisplayPerPage2"]/option']
Li2 = [By.XPATH, '//*[@class=\'content-body-tab\']/div[2]/div[2]/ul/li']
PN2 = [By.XPATH, '//*[@class=\'content-body-tab\']/div[2]/div[2]/ul/li/a']
C_List = [By.XPATH, '//*[@class="content-body-tab"]/table/tbody[1]/tr']
STR = [By.XPATH, '//*[@class="content-body-tab"]/div[2]/div[1]/strong[2]']
SFR = [By.XPATH, '//*[@class="content-body-tab"]/div[2]/div[1]/strong[1]']
Order_Name = [By.LINK_TEXT, 'Community/District Name']
Order_No = [By.LINK_TEXT, 'District Number']
Order_Funding = [By.LINK_TEXT, 'Funding by']
Order_Status = [By.LINK_TEXT, 'Status']

# View Community
View = [By.CSS_SELECTOR, '.view-btn']
VB = [By.ID, 'btnBack']

# Edit Community
Edit = [By.CSS_SELECTOR, '.pencil-btn']

# Community/District Approved Features

ADE = [By.XPATH, '//*[@id=\'Areas_Community_Views_Community_FeaturesCli\']/div[2]/div[1]/div[3]/input']

PREKK = [By.XPATH, '//*[@id=\'Areas_Community_Views_Community_FeaturesCli\']/div[4]/div[1]/div[1]/input']
PREK = [By.XPATH, '//*[@id=\'Areas_Community_Views_Community_FeaturesCli\']/div[6]/div[1]/div[1]/div[1]/input']

Features_Can_Btn = [By.XPATH, '//*[@id=\'Areas_Community_Views_Community_FeaturesCli\']/div[8]/button[2]']
Features_Can_Btn_Can = [By.XPATH, '//*[@id="messageContainer"]/div/p[2]/button[2]']
Features_Can_Btn_Clo = [By.XPATH, '//*[@id="messageContainer"]/div/p[2]/button[1]']
Features_X = [By.XPATH, '//*[@id="modalLarge"]/div/div/div[1]/button']

# Assign Schools
AS = [By.CSS_SELECTOR, '.assign-btn']
DPP = [By.XPATH, '//*[@id="list_Unassignd_ddlDisplayPerPage"]/option']
Li = [By.XPATH, '//*[@id="Areas_Community_Views_Community_AssignSchools1"]/div[1]/div[3]/div[1]/ul/li']
PN = [By.XPATH, '//*[@id="Areas_Community_Views_Community_AssignSchools1"]/div[1]/div[3]/div[1]/ul/li/a']
Order_SN = [By.LINK_TEXT, 'School Name']

Una_SA = [By.ID, 'chkSelectAll']
StoC = [By.XPATH, '//*[@id="Areas_Community_Views_Community_AssignSchools1"]/div[2]/a[1]']
UStoC = [By.XPATH, '//*[@id="Areas_Community_Views_Community_AssignSchools1"]/div[2]/a[2]']
A_SA = [By. ID, 'chkSelectAll2']
Una_Search = [By.XPATH, '//*[@id="Keyword"]']
Una_Search_Btn = [By.XPATH, '//*[@id="Areas_Community_Views_Community_AssignSchools1"]/div[1]/div[2]/button']
# Una_Search_Btn = [By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/div[2]/form/div[1]/div[1]/div[2]/button']
Una_Check = [By.XPATH, '//*[@id="chkSchool0"]']
A_Search = [By.XPATH, '//*[@id="Keyword2"]']
A_Search_Btn = [By.XPATH, '//*[@id="Areas_Community_Views_Community_AssignSchools2"]/div[2]/button']
A_Check = [By.XPATH, '//*[@id="chkSchool20"]']
AB = [By.LINK_TEXT, 'Back']
U_S_List = [By.XPATH, '//*[@id="Areas_Community_Views_Community_AssignSchools1"]/div[1]/table/tbody[1]/tr']
U_STR = [By.XPATH, '//*[@class="content-footer"]/div[2]/strong[2]']
U_SFR = [By.XPATH, '//*[@class="content-footer"]/div[2]/strong[1]']

# Edit Custom Notifications
ECN = [By.CSS_SELECTOR, '.viewcomment-btn']
BtoC = [By.LINK_TEXT, 'Back to Community/District List']
ACN = [By.LINK_TEXT, 'Add Custom Notification']
ACNC = [By.XPATH, '//*[@id="Areas_Community_Views_Community_NewNote"]/div[3]/button[2]']
RequiredStart = [By.ID, 'StartOn-error']
RequiredStop = [By.ID, 'StopOn-error']
RequiredMessages = [By.ID, 'Messages-error']
StartO = [By.ID, 'StartOn']
StopO = [By.ID, 'StopOn']
StatusIn = [By.XPATH, '//*[@id="Status"]/option[2]']
StatusA = [By.XPATH, '//*[@id="Status"]/option[1]']
DL = [By.ID, 'DisplayLogo']
MB = [By.ID, 'Messages-error']
ACNS = [By.XPATH, '//*[@id="Areas_Community_Views_Community_NewNote"]/div[3]/button[1]']
HideShow = [By.CLASS_NAME, 'panel-heading']
ECNE = [By.CSS_SELECTOR, '.pencil-btn']
ECNC = [By.XPATH, '//*[@id="modalLarge"]/div/div/div[1]/button']
ECNCC = [By.XPATH, '//*[@id="messageContainer"]/div/p[2]/button[1]']
ECNS = [By. XPATH, '//*[@id="Areas_Community_Views_Community_EditNote"]/div[3]/button[1]']