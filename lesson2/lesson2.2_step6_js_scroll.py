import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://SunInJuly.github.io/execute_script.html"

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome()
	browser.get(link)
	
	x_selector = browser.find_element_by_id("input_value")
	x = x_selector.text
	
	input = browser.find_element_by_id("answer")
	input.send_keys(calc(x))    
	
	button = browser.find_element_by_css_selector("[type='submit']")
	browser.execute_script("return arguments[0].scrollIntoView(true);", button)
	
	checkbox1 = browser.find_element_by_id("robotCheckbox")
	checkbox1.click()
	
	radiobutton1 = browser.find_element_by_id("robotsRule")
	radiobutton1.click()
	
	button.click()
	
finally:
	time.sleep(10)
	browser.quit()