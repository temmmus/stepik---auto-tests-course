link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_button_is_presented(browser):

    browser.get(link)
    browser.implicitly_wait(5)
    	
    assert browser.find_element_by_class_name("btn-add-to-basket"), "The button is not presented on the page"
