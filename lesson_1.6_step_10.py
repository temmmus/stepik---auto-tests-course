from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/registration1.html"
# link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element_by_css_selector("[placeholder='Input your first name']")
    input1.send_keys("Ivan")    
    input2 = browser.find_element_by_css_selector("[placeholder='Input your last name']")
    input2.send_keys("Ivan")    
    input3 = browser.find_element_by_css_selector("[placeholder='Input your email']")
    input3.send_keys("Ivan")    
    input4 = browser.find_element_by_css_selector("[placeholder='Input your phone:']")
    input4.send_keys("Ivan")    
    input5 = browser.find_element_by_css_selector("[placeholder='Input your address:']")
    input5.send_keys("Ivan")
	
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

finally:
    # time.sleep(10)
    browser.quit()