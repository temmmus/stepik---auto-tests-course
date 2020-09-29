from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
	
	button = browser.find_element_by_tag_name("[type='submit']")
	button.click()
	
	new_window = browser.window_handles[1]
	browser.switch_to.window(new_window)
	
	x_element = browser.find_element_by_id("input_value").text

	input1 = browser.find_element_by_id("answer")
	input1.send_keys(calc(x_element))

	button = browser.find_element_by_css_selector("[type='submit']")
	button.click()
	
finally:
	time.sleep(10)
	browser.quit()