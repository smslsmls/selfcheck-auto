from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from dataclasses import dataclass
import time

class profile:
    school : string = None
    name : string = None
    birth : string = None
    pw : string = None

student=profile()
student.school ="대구소프트웨어고등학교"
student.name="윤서준"
student.birth="051223"
student.pw="1223"
driver = webdriver.Chrome()
driver.get('https://hcs.eduro.go.kr/#/relogin')
driver.find_element_by_id('btnConfirm2').click()
driver.implicitly_wait(1)
driver.find_element_by_class_name('searchBtn').click()
Select(driver.find_element_by_id('sidolabel')).select_by_index(3)
Select(driver.find_element_by_id('crseScCode')).select_by_index(4)
driver.find_element_by_id('orgname').send_keys(student.school)#학교 입력
driver.find_element_by_class_name('searchBtn').click()
driver.find_element_by_xpath("//a[@href='javascript:;']").click()
driver.find_element_by_class_name('layerFullBtn').click()
driver.find_element_by_id('user_name_input').send_keys(student.name)#이름 입력
driver.find_element_by_id('birthday_input').send_keys(student.birth)#생년월일 입력
driver.find_element_by_id('btnConfirm').click()
time.sleep(1)
driver.find_element_by_xpath("//input[@class='input_text_common']").send_keys(student.pw)#입력
driver.find_element_by_id('btnConfirm').click()
time.sleep(1)
driver.find_element_by_class_name('name').click()
time.sleep(1)
driver.find_element_by_id('survey_q1a1').click()
driver.find_element_by_id('survey_q2a1').click()
driver.find_element_by_id('survey_q3a1').click()
driver.find_element_by_id('btnConfirm').click()
