import math
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла


link="http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
browser.get(link)

w=browser.find_element(By.TAG_NAME, "button")
w.click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
s=browser.find_element(By.CSS_SELECTOR, "span#input_value")
m=s.text
x=browser.find_element(By.TAG_NAME, "input")
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x.send_keys(calc(m))
d=browser.find_element(By.TAG_NAME, "button")
d.click()
