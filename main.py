from selenium import webdriver
from selenium.webdriver.common.by import By
import time

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
next_Button.click()

Lastname = "Adukwulu"
Firstname = "Nonso"
DOB ="23/09/87"
Passport_number = "B01502427"
Sex = "male"
Street = "11 Igwe street, Rumuodumanya, Obio/Akpo, Rivers State, Nigeria"
Zip_code1 = "500"
Zip_code2 = "102"
Country = "Nigeria"
Telephone = "08035502017"
Email = "nonsoadukwulunonso@gmail.com"
Name_at_birth ="Nonso"
Nationality_at_birth = "Nigerian"
Country_of_birth = "Nigeria"
Place_of_birth = "Enugu State Nigeria"
Actual_nationality = "Nigerian"
Date_of_issue_of_passport = "12/13/2022"
Passport_valid_until = "12/12/2027"
Passport_issued_at = "Ilorin"


lastname = web.find_element(By.XPATH, '//*[@id="Lastname"]')
lastname.send_keys(Lastname)
firstname = web.find_element(By.XPATH, '//*[@id="Firstname"]')
firstname.send_keys(Firstname)
dOB = web.find_element(By.XPATH, '//*[@id="DateOfBirth"]')
dOB.send_keys(DOB)
sex = web.find_element(By.XPATH, '//*[@id="TraveldocumentNumber"]')
sex.send_keys(Passport_number)
street = web.find_element(By.XPATH, '//*[@id="TraveldocumentNumber"]')
street.send_keys(Passport_number)
zipCode1 = web.find_element(By.XPATH, '//*[@id="TraveldocumentNumber"]')
zipCode1.send_keys(Passport_number)
zipCode2 = web.find_element(By.XPATH, '//*[@id="TraveldocumentNumber"]')
zipCode2.send_keys(Passport_number)
country = web.find_element(By.XPATH, '//*[@id="TraveldocumentNumber"]')
country.send_keys(Passport_number)
telephone = web.find_element(By.XPATH, '//*[@id="TraveldocumentNumber"]')
telephone.send_keys(Passport_number)
email = web.find_element(By.XPATH, '//*[@id="TraveldocumentNumber"]')
email.send_keys(Passport_number)
nameAtBirth = web.find_element(By.XPATH, '//*[@id="TraveldocumentNumber"]')
nameAtBirth.send_keys(Passport_number)
nationalityAtBirth = web.find_element(By.XPATH, '//*[@id="TraveldocumentNumber"]')
nationalityAtBirth.send_keys(Passport_number)
countryOfBirth = web.find_element(By.XPATH, '//*[@id="TraveldocumentNumber"]')
countryOfBirth.send_keys(Passport_number)
place_of_birth = web.find_element(By.XPATH, '//*[@id="TraveldocumentNumber"]')
place_of_birth.send_keys(Passport_number)
actual_nationality = web.find_element(By.XPATH, '//*[@id="TraveldocumentNumber"]')
actual_nationality.send_keys(Passport_number)
date_of_issue_of_passport = web.find_element(By.XPATH, '//*[@id="TraveldocumentNumber"]')
date_of_issue_of_passport.send_keys(Passport_number)
passport_valid_until = web.find_element(By.XPATH, '//*[@id="TraveldocumentNumber"]')
passport_valid_until.send_keys(Passport_number)
passport_issued_at = web.find_element(By.XPATH, '//*[@id="TraveldocumentNumber"]')
passport_issued_at.send_keys(Passport_number)

time.sleep(2)
