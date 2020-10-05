from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link_task = "http://suninjuly.github.io/alert_accept.html"
link_stepik = "https://stepik.org/lesson/184253/step/2?unit=158843"

try:
	browser = webdriver.Chrome()
	browser.get(link_task)
	
	button = browser.find_element_by_tag_name("[type='submit']")
	button.click()
	
	alert = browser.switch_to.alert
	alert.accept() 
	
	x_element = browser.find_element_by_id("input_value").text

	input1 = browser.find_element_by_id("answer")
	input1.send_keys(calc(x_element))

	button = browser.find_element_by_css_selector("[type='submit']")
	button.click()
	
	# alert = browser.switch_to.alert
	# answer = alert.text.split(': ')[-1]
	# alert.accept()
	
	browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't') 
	browser.get(link_stepik)
	
	# input_stepik = browser.find_element_by_id("ember5618")
	# input1.send_keys(answer)
	
finally:
	time.sleep(10)
	browser.quit()