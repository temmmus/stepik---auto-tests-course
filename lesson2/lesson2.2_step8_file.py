from selenium import webdriver
from selenium.webdriver.common.by import By
import os 

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'test_files/1.txt')

link = "http://suninjuly.github.io/file_input.html"


try:
	browser = webdriver.Chrome()
	browser.get(link)
	
	input1 = browser.find_element_by_tag_name("[name='firstname']")
	input1.send_keys("test")    
	
	input2 = browser.find_element_by_tag_name("[name='lastname']")
	input2.send_keys("test")    
	
	input3 = browser.find_element_by_tag_name("[name='email']")
	input3.send_keys("test")    
	
	file_element = browser.find_element_by_id("file")
	file_element.send_keys(file_path)
	
	button = browser.find_element_by_css_selector("[type='submit']")
	button.click()
	
finally:
	time.sleep(10)
	browser.quit()