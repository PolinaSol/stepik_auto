import math
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
link="http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(link)

x1 = browser.find_element_by_id("num1")
x2 = x1.text
x11 = browser.find_element_by_id("num2")
x22 = x11.text
y=int(x2)+int(x22)
print(y)

d=str(y)

select = Select(browser.find_element_by_id("dropdown"))
select.select_by_visible_text(d) # ищем элемент с текстом "Python"

option1 = browser.find_element_by_css_selector("button")
option1.click()