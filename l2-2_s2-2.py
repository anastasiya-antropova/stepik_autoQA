import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
#link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

num1_txt = browser.find_element(By.ID,"num1")
num1=num1_txt.text
num2_txt = browser.find_element(By.ID,"num2")
num2=num2_txt.text

def calc(num1):
    return str(int(num1)+int(num2))

sum=calc(num1)

select = Select(browser.find_element(By.TAG_NAME, "select"))
#select.select_by_value(sum)
select.select_by_visible_text(sum) #ищет элемент по видимому тексту
#select.select_by_index(sum) #ищет элемент по его индексу или порядковому номеру

button1=browser.find_element(By.CLASS_NAME, "btn")
button1.click()

time.sleep(5)
browser.quit()
