import math
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
link="http://suninjuly.github.io/execute_script.html"

browser = webdriver.Chrome()
browser.get(link)

x1 = browser.find_element_by_id("input_value")
x = x1.text
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser.execute_script("window.scrollBy(0, 200);")
p=browser.find_element_by_css_selector("input#answer")
p.send_keys(calc(x))

option1 = browser.find_element_by_css_selector("[id='robotCheckbox']")
option1.click()

option1 = browser.find_element_by_css_selector("[value='robots']")
option1.click()

option1 = browser.find_element_by_css_selector("button")
option1.click()
