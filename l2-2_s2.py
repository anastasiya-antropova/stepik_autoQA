import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link="http://suninjuly.github.io/selects1.html"
#link="http://suninjuly.github.io/selects2.html"

browser = webdriver.Chrome()
browser.get(link)

#browser.find_element(By.TAG_NAME, "select").click() #лишний клик на раскрытие??
browser.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
#browser.find_element(By.CSS_SELECTOR, "[value='1']").click()

#button1=browser.find_element(By.CLASS_NAME, "btn")
#button1.click()

time.sleep(5)
browser.quit()
