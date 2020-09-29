import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
		
	treasure_element = browser.find_element_by_id("treasure")
	x = treasure_element.get_attribute("valuex")
		
	input1 = browser.find_element_by_id("answer")
	input1.send_keys(calc(x))    
	
	checkbox1 = browser.find_element_by_id("robotCheckbox")
	checkbox1.click()
	
	radiobutton1 = browser.find_element_by_id("robotsRule")
	radiobutton1.click()
	
	button = browser.find_element_by_css_selector("[type='submit']")
	button.click()
	
finally:
	time.sleep(10)
	browser.quit()