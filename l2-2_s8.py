from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

with open("test.txt", "w") as file:
    content = file.write("automationbypython")  # create test.txt file

link=('http://suninjuly.github.io/file_input.html')
browser=webdriver.Chrome()
browser.get(link)

firstname=browser.find_element(By.NAME, "firstname")
firstname.send_keys('Test1')
lastname=browser.find_element(By.NAME, "lastname")
lastname.send_keys('Test2')
email=browser.find_element(By.NAME, "email")
email.send_keys("test@test.tt")

file=browser.find_element(By.ID, "file")
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла
file.send_keys(file_path)

print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))

button=browser.find_element(By.TAG_NAME, "button")
button.click()

time.sleep(15)
browser.quit
