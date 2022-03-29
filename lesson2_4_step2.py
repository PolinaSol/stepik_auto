from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")
browser.execute_script("window.scrollBy(0, 500);")
WebDriverWait(browser, 12).until( EC.text_to_be_present_in_element((By.ID, "price"),'$100'  ))

btn = browser.find_element_by_id("book")
btn.click()
browser.execute_script("window.scrollBy(0, 800);")

s=browser.find_element(By.CSS_SELECTOR, "span#input_value")
m=s.text
x=browser.find_element(By.TAG_NAME, "input")
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x.send_keys(calc(m))
d=browser.find_element(By.CSS_SELECTOR, "button#solve")
d.click()