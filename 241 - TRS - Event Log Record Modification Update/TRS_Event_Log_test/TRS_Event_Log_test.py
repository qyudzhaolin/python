import pytest
import sys, random, string, time
sys.path.append('..')
from login_opt import *
from config.ELEMENTS_TRS_EVENT_LOG import *
from selenium.webdriver.common.keys import Keys
from lib.db_mg import DatabaseManagement



def check_TRS(driver):
	driver.find_element(txtCommunity[0], txtCommunity[1]).send_keys(Community_Name)
	driver.find_element(Community_Search_Btn[0], Community_Search_Btn[1]).click()
	sleep(2)
	driver.find_element(Features[0], Features[1]).click()
	sleep(1)
	driver.find_element(TRS[0], TRS[1]).click()
	driver.find_element(Features_Sub_Btn[0], Features_Sub_Btn[1]).click()

def randomName(size):
	char_lists = string.ascii_letters
	return ''.join(random.choice(char_lists) for _ in range(size))

def randomDropDownList(driver, element):
	all_ele = driver.find_elements(element[0], element[1])
	select_ele_index = random.randint(1, len(all_ele) - 1)
	all_ele[select_ele_index].click()
	sleep(1)

def randomNumber(size):
	return ''.join(random.choice(string.digits) for _ in range(size))

def phoneNumber(driver, element):
	driver.find_element(element[0], element[1]).click()
	sleep(1)
	driver.find_element(element[0], element[1]).send_keys(Keys.LEFT*10, randomNumber(10))

def add_trs_specialist(driver):
	driver.find_element(User_M[0], User_M[1]).click()
	sleep(1)
	driver.find_element(TRS_Specialist[0], TRS_Specialist[1]).click()
	sleep(1)
	driver.find_element(Add_btn[0], Add_btn[1]).click()
	sleep(1)
	driver.find_element(txtCommunity[0], txtCommunity[1]).send_keys(Community_Name)
	sleep(1)
	driver.find_element(txtSchool[0], txtSchool[1]).send_keys(School_Name)
	sleep(1)
	fName = randomName(5)
	driver.find_element(First_Name[0], First_Name[1]).send_keys(fName)
	lName = randomName(10)
	driver.find_element(Last_Name[0], Last_Name[1]).send_keys(lName)
	randomDropDownList(driver, Title_Role)
	driver.find_element(Address[0], Address[1]).send_keys('9990 Richmond Ave. North Building, Ste 180.')
	randomDropDownList(driver, State)
	sleep(1)
	randomDropDownList(driver, County)
	phoneNumber(driver, Primary_Phone_Number)
	randomDropDownList(driver, Primary_Number_Type)
	driver.find_element(Primary_Email[0], Primary_Email[1]).send_keys('cs@sunnet.us')
	driver.find_element(Submit[0], Submit[1]).click()
	sleep(3)
	return fName, lName

def drop_down_list(driver, element, value):
	return driver.find_element(element[0], element[1]).find_element_by_css_selector("option[value='%s']" % value)

def get_into_event_log_page(driver):
	driver.find_element(TRS_A_Tool[0], TRS_A_Tool[1]).click()
	sleep(2)
	driver.find_element(txtCommunity[0], txtCommunity[1]).send_keys(Community_Name)
	sleep(2)
	driver.find_element(txtSchool[0], txtSchool[1]).send_keys(School_Name)
	sleep(1)
	driver.find_element(TRS_A_Tool_Search_Btn[0], TRS_A_Tool_Search_Btn[1]).click()
	sleep(1)
	driver.find_element(TRS_A_Tool_Play_Btn[0], TRS_A_Tool_Play_Btn[1]).click()
	sleep(1)
	driver.find_element(Event_Log[0], Event_Log[1]).click()
	sleep(1)

def create_event(driver):
	driver.find_element(Create_Event_Btn[0], Create_Event_Btn[1]).click()
	sleep(1)
	driver.find_element(Date_Created[0], Date_Created[1]).send_keys(time.strftime("%m/%d/%Y"))
	driver.find_element(Created_By[0], Created_By[1]).send_keys(randomName(6))
	driver.find_element_by_xpath('//*[@id="EventType0"]/option[%s]' % (random.choice((2, 3, 4, 6, 7, 9, 10, 11)))).click()
	driver.find_element(Event_Log_Save_Btn[0], Event_Log_Save_Btn[1]).click()
	sleep(2)

def modify_notification(driver):
	driver.find_element(Modified_Btn[0], Modified_Btn[1]).click()
	sleep(1)
	driver.find_element(check_Notification[0], check_Notification[1]).click()
	driver.find_element(Event_Log_Save_Btn[0], Event_Log_Save_Btn[1]).click()
	sleep(5)
	driver.find_element(close_btn[0], close_btn[1]).click()
	sleep(1)
	driver.find_element(Modified_Btn[0], Modified_Btn[1]).click()
	sleep(1)
	driver.find_element(check_Notification[0], check_Notification[1]).click()
	driver.find_element(Event_Log_Save_Btn[0], Event_Log_Save_Btn[1]).click()
	sleep(1)

def star_level_change(driver):
	driver.find_element(Modified_Btn[0], Modified_Btn[1]).click()
	sleep(2)
	driver.find_element(edit_Star_Level_Change[0], edit_Star_Level_Change[1]).click()
	sleep(2)
	selected_star = driver.find_elements(selected[0], selected[1])[1]
	print('selected star is ', selected_star.text)
	get_value = selected_star.get_attribute('value')
	print(get_value)
	value_list = [1, 2, 3, 4]
	print(value_list)
	value_list.remove(int(get_value))
	print(value_list)
	driver.find_element_by_xpath('//*[@id="verifiedStar"]/option[%s]' % (random.choice(value_list))).click()

	driver.find_element(approval_date[0], approval_date[1]).send_keys(time.strftime("%m/%d/%Y"))
	driver.find_element(recertification_date[0], recertification_date[1]).send_keys(time.strftime("%m/%d/%Y"))
	driver.find_element(Submit[0], Submit[1]).click()
	sleep(1)
	driver.find_element(change_btn[0], change_btn[1]).click()
	sleep(1)
	driver.find_element(comment[0], comment[1]).send_keys(randomName(5))
	driver.find_element(Event_Log_Save_Btn[0], Event_Log_Save_Btn[1]).click()
	sleep(10)
	driver.find_element(close_btn[0], close_btn[1]).click()
	sleep(1)

def auto_assign(driver):
	driver.find_element(Modified_Btn[0], Modified_Btn[1]).click()
	sleep(2)
	driver.find_element(edit_auto_assign[0], edit_auto_assign[1]).click()
	sleep(1)
	driver.find_element_by_xpath('//*[@id="Areas_Trs_Views_Index_Accreditations"]/div[%s]/div/div/label' % (random.randint(1, 8))).click()

	all_ele = driver.find_elements(verified_star_designation[0], verified_star_designation[1])
	print('all ele: ', len(all_ele))
	select_ele_index = random.randint(0, len(all_ele) - 1)
	select_ele = all_ele[select_ele_index]
	select_ele.click()

	driver.find_element(approval_date[0], approval_date[1]).send_keys(time.strftime("%m/%d/%Y"))
	driver.find_element(recertification_date[0], recertification_date[1]).send_keys(time.strftime("%m/%d/%Y"))

	driver.find_element(Submit[0], Submit[1]).click()
	driver.find_element(check_Notification[0], check_Notification[1]).click()
	driver.find_element(Event_Log_Save_Btn[0], Event_Log_Save_Btn[1]).click()
	sleep(2)


class TestCommunityTRS:

	def test_login(self, login):
		driver = login
		sleep(1)
		driver.find_element(Class_Student_Management[0], Class_Student_Management[1]).click()

	def test_community_trs(self, login):
		db_se = DatabaseManagement()
		try:
			db_se.check_community_trs()
			print('The Community has been checked TRS.')
			sleep(1)
		except:
			print('Should check the TRS for the Community')
			check_TRS(login)
			sleep(1)

	def test_add_two_trs_specialist(self, login):
		global User_1, User_1_ID, User_2, User_2_ID
		db_se = DatabaseManagement()

		fName_1, lName_1 = add_trs_specialist(login)
		User_1 = fName_1 + ' ' + lName_1
		User_1_ID_data = db_se.user_id(fName_1, lName_1)
		User_1_ID = User_1_ID_data.ID
		print('User 1: %s %s' % (fName_1, lName_1), 'ID: %s' % User_1_ID)

		fName_2, lName_2 = add_trs_specialist(login)
		User_2 = fName_2 + ' ' + lName_2
		User_2_ID_data = db_se.user_id(fName_2, lName_2)
		User_2_ID = User_2_ID_data.ID
		print('User 2: %s %s' % (fName_2, lName_2), 'ID: %s' % User_2_ID)

	def test_add_trs_class(self, login):
		driver = login
		driver.find_element(TRS_Class_M[0], TRS_Class_M[1]).click()
		sleep(1)
		driver.find_element(Add_btn[0], Add_btn[1]).click()
		sleep(1)
		driver.find_element(txtSchool[0], txtSchool[1]).send_keys(School_Name)
		sleep(1)
		driver.find_element(Class_Name[0], Class_Name[1]).send_keys(randomName(15))
		drop_down_list(login, Assessor, User_1_ID).click()
		drop_down_list(login, Mentor, User_2_ID).click()
		driver.find_element(AoC0m[0], AoC0m[1]).click()
		driver.find_element(AoC18m[0], AoC18m[1]).click()
		driver.find_element(AoC3y[0], AoC3y[1]).click()
		driver.find_element(AoC5y[0], AoC5y[1]).click()
		driver.find_element(Submit[0], Submit[1]).click()
		sleep(2)

	def test_edit_school(self, login):
		driver = login
		driver.find_element(School_Management[0], School_Management[1]).click()
		sleep(1)
		driver.find_element(txtCommunity[0], txtCommunity[1]).send_keys(Community_Name)
		sleep(1)
		driver.find_element(School_txtSchool[0], School_txtSchool[1]).send_keys(School_Name)
		driver.find_element(School_Search_Btn[0], School_Search_Btn[1]).click()
		sleep(2)
		driver.find_element(School_Edit[0], School_Edit[1]).click()
		sleep(2)
		drop_down_list(login, Assessor, User_1_ID).click()
		sleep(5)
		driver.find_element(Submit[0], Submit[1]).click()
		sleep(2)
		driver.find_element(LOGOUT[0], LOGOUT[1]).click()


class TestOtherUserslogin:
	def test_other_users_login(self, login):
		driver = login
		print(User_1, User_1_ID, User_2, User_2_ID)

		login_user(str(User_1_ID))
		get_into_event_log_page(login)
		create_event(login)
		# modify_notification(login)
		star_level_change(login)
		auto_assign(login)

		login_user(str(User_2_ID))
		get_into_event_log_page(login)
		create_event(login)
		# modify_notification(login)
		star_level_change(login)
		auto_assign(login)

		driver.quit()