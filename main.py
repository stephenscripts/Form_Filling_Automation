from selenium import webdriver
from selenium.webdriver.common.by import By
import time
person = {
    "Last name": "Adukwulu",
    "First name": "Nonso",
    "Date of birth": "23/09/87",
    "Passport number": "B01502427",
    "Sex": "male",
    "Street": "11 Igwe street, Rumuodumanya, Obio/Akpo, Rivers State, Nigeria",
    "Zip code": 500102
Country: Nigeria
Telephone: 08035502017
E-mail: nonsoadukwulunonso@gmail.com
Name at birth: Nonso
Nationality at birth: Nigerian
Country of birth: Nigeria
Place of birth: Enugu State Nigeria
Actual nationality: Nigerian
Date of issue of passport:13 Dec/Dec 22
Passport valid until:12 Dec/Dec 27
Passport issued by (authority): Ilorin

}

web = webdriver.Chrome()
web.get('https://appointment.bmeia.gv.at/')

time.sleep(1)

countries = web.find_element(By.XPATH, '//*[@id="Office"]/option[2]')
countries.click()
next_Button = web.find_element(By.XPATH, '//*[@id="main"]/form/table[2]/tbody/tr[2]/td[2]/input')
next_Button.click()
time.sleep(1)

verification_legalization = web.find_element(By.XPATH, '//*[@id="CalendarId"]/option[3]')
verification_legalization.click()
next_Button = web.find_element(By.XPATH, '//*[@id="main"]/form/table[2]/tbody/tr[3]/td[2]/input[2]')
next_Button.click()
time.sleep(1)

number_of_persons = web.find_element(By.XPATH, '//*[@id="PersonCount"]/option[1]')
number_of_persons.click()
next_Button = web.find_element(By.XPATH, '//*[@id="main"]/form/table[2]/tbody/tr[4]/td[2]/input[2]')
next_Button.click()

next_Button = web.find_element(By.XPATH, '//*[@id="main"]/form/input[6]')
next_Button.click()
time.sleep(3)

next_Button = web.find_element(By.XPATH, '//*[@id="main"]/form/input[7]')

time.sleep(2)
