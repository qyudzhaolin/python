import pytest
import sys, random, string, time
sys.path.append('..')
from login_opt import *
from config.ELEMENTS_EXPAND_COLLAPSE import *
from selenium.webdriver.common.keys import Keys
from lib.db_mg import DatabaseManagement






class TestCommunityTRS:

	def test_login(self, login):
		driver = login
		sleep(1)

	def test_community_trs(self, login):
		# login_user('hunk@sunnet.us', 'a1316191111?')
		login_user('30325')  # 输入对应的user id
