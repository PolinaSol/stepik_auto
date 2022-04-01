import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec




@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    #browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('add', [

"https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"  ])
def test_guest_should_see_login_link(browser, add):
    link = add
    browser.get(link)
    WebDriverWait(browser, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "textarea")))
    a = browser.find_element_by_css_selector("textarea")
    answer = math.log(int(time.time()+5))
    a.send_keys(str(answer))
    d=    browser.find_element_by_css_selector(".submit-submission")
    d.click()

    #WebDriverWait(browser, 5).until( ec.text_to_be_present_in_element((By.CSS_SELECTOR, ".smart-hints__hint"),'Correct!'  ))
    WebDriverWait(browser, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, ".attempt-message_correct")))
    #  .attempt-message_correct

    f=browser.find_element(By.CSS_SELECTOR,".smart-hints__hint")
    assert "Correct!" in f.text, f"oshibka nado Correct, a prislo {f.text}"