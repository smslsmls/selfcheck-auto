from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time


driver = webdriver.Chrome()
driver.get('https://hcs.eduro.go.kr/#/relogin')
driver.find_element_by_id('btnConfirm2').click()
driver.implicitly_wait(1)
driver.find_element_by_class_name('searchBtn').click()
Select(driver.find_element_by_id('sidolabel')).select_by_index(3)
Select(driver.find_element_by_id('crseScCode')).select_by_index(4)
driver.find_element_by_id('orgname').send_keys('대구소프트웨어마이스터고등학교')#학교 입력
driver.find_element_by_class_name('searchBtn').click()
driver.find_element_by_xpath("//a[@href='javascript:;']").click()
driver.find_element_by_class_name('layerFullBtn').click()
driver.find_element_by_id('user_name_input').send_keys('윤서준')#이름 입력
driver.find_element_by_id('birthday_input').send_keys('051223')#생년월일 입력
driver.find_element_by_id('btnConfirm').click()
time.sleep(1)
driver.find_element_by_xpath("//input[@class='input_text_common']").send_keys('1223')#비밀번호 입력
driver.find_element_by_id('btnConfirm').click()
time.sleep(1)
driver.find_element_by_class_name('name').click()
time.sleep(1)
driver.find_element_by_id('survey_q1a1').click()
driver.find_element_by_id('survey_q2a1').click()
driver.find_element_by_id('survey_q3a1').click()
driver.find_element_by_id('btnConfirm').click()
