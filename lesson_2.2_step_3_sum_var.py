import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
		
	num1 = browser.find_element_by_id("num1")
	x = num1.text
	
	num2 = browser.find_element_by_id("num2")
	y = num2.text
	
	sum = int(x) + int(y)
	
	select = Select(browser.find_element_by_id("dropdown"))
	select.select_by_value(str(sum)) 
				
	button = browser.find_element_by_css_selector("[type='submit']")
	button.click()
	
finally:
	time.sleep(10)
	browser.quit()