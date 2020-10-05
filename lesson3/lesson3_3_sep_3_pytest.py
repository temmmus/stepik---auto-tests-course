import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Tests(unittest.TestCase):
    def test_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        
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
        # time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "fuuuuuu")
        browser.quit()
        
    def test_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        
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
        # time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "fuuuuuu")
        browser.quit()

if __name__ == "__main__":
    unittest.main()
