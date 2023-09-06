import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_button_add_to_cart_is_present(browser):
    browser.get(link)
    button = len(browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket"))
    assert button > 0,  'The button was not found' 