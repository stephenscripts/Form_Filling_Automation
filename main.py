from selenium import webdriver
from selenium.webdriver.common.by import By
import time

web = webdriver.Chrome()
web.get('https://appointment.bmeia.gv.at/')

time.sleep(2)

countries = web.find_element(By.XPATH, '//*[@id="Office"]/option[2]')
countries.click()
next_Button = web.find_element(By.XPATH, '//*[@id="main"]/form/table[2]/tbody/tr[2]/td[2]/input')
next_Button.click()
time.sleep(2)

verification_legalization = web.find_element(By.XPATH, '//*[@id="CalendarId"]/option[3]')
verification_legalization.click()
next_Button = web.find_element(By.XPATH, '//*[@id="main"]/form/table[2]/tbody/tr[3]/td[2]/input[2]')
next_Button.click()
time.sleep(2)

number_of_persons = web.find_element(By.XPATH, '//*[@id="PersonCount"]/option[1]')
number_of_persons.click()
next_Button = web.find_element(By.XPATH, '//*[@id="main"]/form/table[2]/tbody/tr[4]/td[2]/input[2]')
next_Button.click()

next_Button = web.find_element(By.XPATH, '//*[@id="main"]/form/input[6]')
next_Button.click()
time.sleep(2)
