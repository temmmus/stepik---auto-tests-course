import time
import math
import pytest
from selenium import webdriver



@pytest.fixture(scope="function")
def browser():

    print("\nstart browser for test..")
    browser = webdriver.Chrome()

    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('page_number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
# @pytest.mark.parametrize('page_number', ["236895"])
def test_send_answer(browser, page_number):

    link = f"https://stepik.org/lesson/{page_number}/step/1"
    browser.get(link)
	
    browser.implicitly_wait(5)
	
    input = browser.find_element_by_tag_name("textarea")
    input.send_keys(str(math.log(int(time.time()))))

    button = browser.find_element_by_class_name("submit-submission")
    button.click()
	
    assert browser.find_element_by_class_name("smart-hints__hint").text == "Correct!", "Jopa"
	
	
    # time.sleep(30)

