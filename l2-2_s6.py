from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link=('http://suninjuly.github.io/execute_script.html')
browser=webdriver.Chrome()
browser.get(link)

x1=browser.find_element(By.ID, "input_value")
x=x1.text

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

y=calc(x)
y_el=browser.find_element(By.ID, "answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", y_el)
y_el.send_keys(y)

ch_box=browser.find_element(By.ID, "robotCheckbox")
ch_box.click()

radio=browser.find_element(By.ID, "robotsRule")
radio.click()

button=browser.find_element(By.TAG_NAME, "button")
#browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

time.sleep(15)
browser.quit()