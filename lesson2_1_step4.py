import math
from selenium import webdriver
from selenium.webdriver.common.by import By
link=" http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id("treasure")
x = x_element.get_attribute("valuex")


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

p=browser.find_element_by_css_selector("input#answer")
p.send_keys(calc(x))

option1 = browser.find_element_by_css_selector("[id='robotCheckbox']")
option1.click()

option1 = browser.find_element_by_css_selector("[value='robots']")
option1.click()

option1 = browser.find_element_by_css_selector("button")
option1.click()