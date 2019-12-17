from selenium import webdriver
from time import sleep
import random
from config.ELEMENT_ADD_Teacher import *
from config.ELEMENTS_COMMUNITY import Class_Student_Management, LOGOUT, Mainsite_Url
from config.ELEMENTS_USER_MANAGEMENT import *
from config.ELEMENTS_DASHBOARD import *
from config.ELEMENT_MYPROFILE import *
from config.ELEMENT_PRAC_CDUSER_Registry import *
from config.ELEMENT_ADD_PRINCIPAL import *
from lib.db_mg import *
from login_opt import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

def random_char():
    Name = ""
    for i in range(5):
        index = random.randint(97, 122)
        Name = Name + chr(index)
    return Name


class Test_Optin():

    def test_login(self, login):
        sleep(2)
        login.find_element(Class_Student_Management[0], Class_Student_Management[1]).click()
        sleep(2)
        location = login.current_url
        if location == Mainsite_Url:
            print("We are now at mainsite!")
        else:
            assert False
    # Add Teacher
    def test_add_teacher(self, login):
        global FirstName, LastName
        FirstName = random_char()
        LastName = random_char()
        # 访问User Management
        login.find_element(User_Management[0], User_Management[1]).click()
        sleep(1)
        # 访问Teacher列表页
        login.find_element(Teacher[0], Teacher[1]).click()
        sleep(1)
        # 打开Add teacher 页面
        login.find_element(Add_Teacher_Button[0], Add_Teacher_Button[1]).click()
        # 输入各字段信息
        login.find_element(Add_Teacher_Community[0], Add_Teacher_Community[1]).send_keys("CLI TEST COMMUNITY")
        login.find_element(Add_Teacher_School[0], Add_Teacher_School[1]).send_keys("Test School 1")
        login.find_element(Add_Teacher_FirstName[0], Add_Teacher_FirstName[1]).send_keys(FirstName)
        login.find_element(Add_Teacher_LastName[0], Add_Teacher_LastName[1]).send_keys(LastName)
        login.find_element(Add_Teacher_PrimaryEmail[0], Add_Teacher_PrimaryEmail[1]).send_keys("Test@" + random_char() + ".com")
        login.find_element(Add_Teacher_Submit[0], Add_Teacher_Submit[1]).click()
        # 退出登录
        login.find_element(Logout_Link[0], Logout_Link[1]).click()

    # 登录新建teacher
    def test_teacher_login(self):
        DBteacher = DataManagement()
        browser = login_user(str(DBteacher.test_user_id(FirstName, LastName).ID))
        browser.find_element(Opt_Do_WorkInTexas_No[0], Opt_Do_WorkInTexas_No[1]).click()
        browser.find_element(Opt_Do_WorkInEarly_No[0], Opt_Do_WorkInEarly_No[1]).click()
        browser.find_element(Opt_Save_Change_Button[0], Opt_Save_Change_Button[1]).click()
        sleep(1)
        # 访问My Profile页面
        browser.find_element(My_Profile[0], My_Profile[1]).click()
        sleep(3)
        browser.find_element(Tecpds_Status[0], Tecpds_Status[1]).click()
        sleep(1)
        browser.find_element(Opt_Do_WorkInTexas_Yes[0], Opt_Do_WorkInTexas_Yes[1]).click()
        browser.find_element(Opt_Do_WorkInEarly_Yes[0], Opt_Do_WorkInEarly_Yes[1]).click()
        browser.find_element(Opt_Role[0], Opt_Role[1]).click()
        browser.find_element(By.XPATH, "//*[@id='Role']/option[3]").click()
        index = random.randint(2, 4)
        browser.find_element(By.XPATH, "//*[@id='AgeGroup']/option[%s]" %index).click()
        select_number = random.randint(2, 5)
        browser.find_element(By.XPATH, "//*[@id='FacilityType']/option[%s]" %select_number).click()
        browser.find_element(Opt_Save_Change_Button[0], Opt_Save_Change_Button[1]).click()
        sleep(3)
        browser.find_element(Opt_No_To_TECPDS[0], Opt_No_To_TECPDS[1]).click()
        browser.find_element(Opt_Save_Change_Button_01[0], Opt_Save_Change_Button_01[1]).click()
        sleep(1)
        browser.find_element(Tecpds_Status[0], Tecpds_Status[1]).click()
        sleep(1)
        browser.find_element(Opt_Save_Change_Button[0], Opt_Save_Change_Button[1]).click()
        sleep(1)
        browser.find_element(Opt_Save_Change_Button_01[0], Opt_Save_Change_Button_01[1]).click()
        sleep(2)
        browser.find_element_by_xpath("//*[@href='/Home/Dashboard' and @ class='main-ade-left-active']").click()
        sleep(2)
        browser.find_element_by_xpath("/html/body/div[3]/div[1]/a[3]").click()
        sleep(1)

    def test_tecpds_login(self):
        DBuser = TecpdsDataManagement()
        UserID = DBuser.query_user_id(FirstName, LastName)
        UserGoogleID = DBuser.query_google_id(UserID)
        index = random.randint(2, 255)
        number_type = random.randint(2, 4)
        browser = teacpds_login(UserGoogleID)
        browser.find_element(Prac_CD_Birth_Date[0], Prac_CD_Birth_Date[1]).send_keys("12/09/2019")
        browser.find_element(Prac_CD_Home_Address[0], Prac_CD_Home_Address[1]).send_keys("Test Home Addresss")
        browser.find_element(Prac_CD_City[0], Prac_CD_City[1]).send_keys("Test City")
        for i in range(0, 5):
            browser.find_element(Prac_CD_Zip_Code[0], Prac_CD_Zip_Code[1]).send_keys(Keys.BACKSPACE)
        browser.find_element(Prac_CD_Zip_Code[0], Prac_CD_Zip_Code[1]).send_keys("66666")
        # value = browser.find_element(Prac_CD_States_Select[0], Prac_CD_States_Select[1]).text
        s1 = Select(browser.find_element_by_id("State"))
        for select in s1.all_selected_options:
            value = select.text
        print(value)
        if value == 'TX':
            browser.find_element(Prac_CD_County[0], Prac_CD_County[1]).click()
            browser.find_element_by_xpath("//*[@id='County']/option[%s]" %index).click()
        for i in range(0, 9):
            browser.find_element(Prac_CD_Primary_Phone_Number[0], Prac_CD_Primary_Phone_Number[1]).send_keys(Keys.BACKSPACE)
        browser.find_element(Prac_CD_Primary_Phone_Number[0], Prac_CD_Primary_Phone_Number[1]).send_keys("9999999999")
        browser.find_element(Prac_CD_Primary_Number_Type[0], Prac_CD_Primary_Number_Type[1]).click()
        browser.find_element_by_xpath("//*[@id='PrimaryNumberType']/option[%s]" %number_type).click()
        browser.find_element(Prac_CD_Submit_Button[0], Prac_CD_Submit_Button[1]).click()
        sleep(2)
        browser.find_element_by_link_text("LOGOUT").click()

    def test_add_principal(self):
        global Principal_FirstName, Principal_LastName
        Principal_FirstName = random_char()
        Principal_LastName = random_char()
        sleep(2)
        browser = login_user("1")
        browser.find_element(Class_Student_Management[0], Class_Student_Management[1]).click()
        sleep(2)
        browser.find_element(User_Management[0], User_Management[1]).click()
        sleep(1)
        browser.find_element(Principal_Director[0], Principal_Director[1]).click()
        sleep(1)
        # 进入添加Principal页面
        browser.find_element(Add_Principal_Button[0], Add_Principal_Button[1]).click()
        sleep(2)
        # 输入各字段信息
        browser.find_element(Add_Principal_Community[0], Add_Principal_Community[1]).send_keys("CLI TEST COMMUNITY")
        browser.find_element(Add_Principal_School[0], Add_Principal_School[1]).send_keys("Test School 1")
        browser.find_element(Add_Principal_FirstName[0], Add_Principal_FirstName[1]).send_keys(Principal_FirstName)
        browser.find_element(Add_Principal_LastName[0], Add_Principal_LastName[1]).send_keys(Principal_LastName)
        browser.find_element(Add_Principal_PrimaryEmail[0], Add_Principal_PrimaryEmail[1]).send_keys("Test@" + random_char() + ".com")
        # 提交Principal
        browser.find_element(Add_Principal_Submit[0], Add_Principal_Submit[1]).click()
        sleep(2)
        # 退出登录
        browser.find_element(Logout_Link[0], Logout_Link[1]).click()

    def test_principal_login(self):
        DBteacher = DataManagement()
        browser = login_user(str(DBteacher.test_user_id(Principal_FirstName, Principal_LastName).ID))
        browser.find_element(Opt_Do_WorkInTexas_No[0], Opt_Do_WorkInTexas_No[1]).click()
        browser.find_element(Opt_Do_WorkInEarly_No[0], Opt_Do_WorkInEarly_No[1]).click()
        browser.find_element(Opt_Save_Change_Button[0], Opt_Save_Change_Button[1]).click()
        sleep(1)
        # 访问My Profile页面
        browser.find_element(My_Profile[0], My_Profile[1]).click()
        sleep(3)
        browser.find_element(Tecpds_Status[0], Tecpds_Status[1]).click()
        sleep(1)
        browser.find_element(Opt_Do_WorkInTexas_Yes[0], Opt_Do_WorkInTexas_Yes[1]).click()
        browser.find_element(Opt_Do_WorkInEarly_Yes[0], Opt_Do_WorkInEarly_Yes[1]).click()
        browser.find_element(Opt_Role[0], Opt_Role[1]).click()
        browser.find_element(By.XPATH, "//*[@id='Role']/option[3]").click()
        index = random.randint(2, 4)
        browser.find_element(By.XPATH, "//*[@id='AgeGroup']/option[%s]" %index).click()
        select_number = random.randint(2, 5)
        browser.find_element(By.XPATH, "//*[@id='FacilityType']/option[%s]" %select_number).click()
        browser.find_element(Opt_Save_Change_Button[0], Opt_Save_Change_Button[1]).click()
        sleep(3)
        browser.find_element(Opt_No_To_TECPDS[0], Opt_No_To_TECPDS[1]).click()
        browser.find_element(Opt_Save_Change_Button_01[0], Opt_Save_Change_Button_01[1]).click()
        sleep(1)
        browser.find_element(Tecpds_Status[0], Tecpds_Status[1]).click()
        sleep(1)
        browser.find_element(Opt_Save_Change_Button[0], Opt_Save_Change_Button[1]).click()
        sleep(1)
        browser.find_element(Opt_Save_Change_Button_01[0], Opt_Save_Change_Button_01[1]).click()
        sleep(1)
        browser.find_element(Logout_Link[0], Logout_Link[1]).click()
        sleep(1)

    def test_tecpds_cduser_login(self):
        DBuser = TecpdsDataManagement()
        UserID = DBuser.query_user_id(Principal_FirstName, Principal_LastName)
        UserGoogleID = DBuser.query_google_id(UserID)
        index = random.randint(2, 255)
        state_index = random.randint(2, 56)
        number_type = random.randint(2, 4)
        browser = tecpds_cduser_login(UserGoogleID)
        browser.find_element(Prac_CD_Birth_Date[0], Prac_CD_Birth_Date[1]).send_keys("12/09/2019")
        browser.find_element(Prac_CD_Home_Address[0], Prac_CD_Home_Address[1]).send_keys("Test Home Addresss")
        browser.find_element(Prac_CD_City[0], Prac_CD_City[1]).send_keys("Test City")
        for i in range(0, 5):
            browser.find_element(Prac_CD_Zip_Code[0], Prac_CD_Zip_Code[1]).send_keys(Keys.BACKSPACE)
        browser.find_element(Prac_CD_Zip_Code[0], Prac_CD_Zip_Code[1]).send_keys("66666")
        # value = browser.find_element(Prac_CD_States_Select[0], Prac_CD_States_Select[1]).text
        browser.find_element_by_xpath("//*[@id='County']/option[%s]" %state_index).click()  # //*[@id="State"]/option[56]
        s1 = Select(browser.find_element_by_id("State"))
        for select in s1.all_selected_options:
            value = select.text
        print(value)
        if value == 'TX':
            browser.find_element(Prac_CD_County[0], Prac_CD_County[1]).click()
            browser.find_element_by_xpath("//*[@id='County']/option[%s]" %index).click()
        for i in range(0, 9):
            browser.find_element(Prac_CD_Primary_Phone_Number[0], Prac_CD_Primary_Phone_Number[1]).send_keys(Keys.BACKSPACE)
        browser.find_element(Prac_CD_Primary_Phone_Number[0], Prac_CD_Primary_Phone_Number[1]).send_keys("9999999999")
        browser.find_element(Prac_CD_Primary_Number_Type[0], Prac_CD_Primary_Number_Type[1]).click()
        browser.find_element_by_xpath("//*[@id='PrimaryNumberType']/option[%s]" %number_type).click()
        browser.find_element(Prac_CD_Submit_Button[0], Prac_CD_Submit_Button[1]).click()
        browser.find_element_by_link_text("LOGOUT").click()
        sleep(2)
        browser.quit()
