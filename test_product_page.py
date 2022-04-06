from pages.base_page import BasePage
from pages.product_page import PageObject
from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from pages.product_page import PageObject
import time
import pytest
'''@pytest.mark.parametrize('link',
                             ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])'''

'''def test_open_b(browser,link):

    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = PageObject(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    #browser.delete_all_cookies()
    page.open()                      # открываем страницу
    #browser.execute_script("window.scrollBy(0, 200);")
    WebDriverWait(browser, 3).until(ec.element_to_be_clickable((By.CSS_SELECTOR, ".btn-add-to-basket")))
    page.add_backet()         # выполняем метод страницы — переходим на страницу логина
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()'''
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = PageObject(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    #browser.delete_all_cookies()
    page.open()                      # открываем страницу
    page.add_backet()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()