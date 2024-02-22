from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

chrome_options = webdriver.ChromeOptions()
settings = {
    "recentDestinations": [{
        "id": "Save as PDF",
        "origin": "local",
        "account": "",
    }],
    "selectedDestinationId": "Save as PDF",
    "version": 2
}
prefs = {'printing.print_preview_sticky_settings.appState': json.dumps(settings)}
chrome_options.add_experimental_option('prefs', prefs)
chrome_options.add_argument('--kiosk-printing')
CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
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
DOB = "23/09/87"
Passport_number = "B01502427"
Sex = "male"
Street = "11 Igwe street, Rumuodumanya, Obio/Akpo, Rivers State, Nigeria"
Zip_code1 = "500"
Zip_code2 = "102"
Telephone = "08035502017"
Email = "nonsoadukwulunonso@gmail.com"
Name_at_birth = "Nonso"
Place_of_birth = "Enugu State Nigeria"
Actual_nationality = "Nigerian"
Date_of_issue_of_passport = "12/13/2022"
Passport_valid_until = "12/12/2027"

lastname = web.find_element(By.XPATH, '//*[@id="Lastname"]')
lastname.send_keys(Lastname)
firstname = web.find_element(By.XPATH, '//*[@id="Firstname"]')
firstname.send_keys(Firstname)
dOB = web.find_element(By.XPATH, '//*[@id="DateOfBirth"]')
dOB.send_keys(DOB)
sex = web.find_element(By.XPATH, '//*[@id="Sex"]/option[3]')
sex.click()
street = web.find_element(By.XPATH, '//*[@id="Street"]')
street.send_keys(Street)
zipCode1 = web.find_element(By.XPATH, '//*[@id="Postcode"]')
zipCode1.send_keys(Zip_code1)
zipCode2 = web.find_element(By.XPATH, '//*[@id="City"]')
zipCode2.send_keys(Zip_code2)
country = web.find_element(By.XPATH, '//*[@id="Country"]/option[164]')
country.click()
telephone = web.find_element(By.XPATH, '//*[@id="Telephone"]')
telephone.send_keys(Telephone)
email = web.find_element(By.XPATH, '//*[@id="Email"]')
email.send_keys(Email)
nameAtBirth = web.find_element(By.XPATH, '//*[@id="LastnameAtBirth"]')
nameAtBirth.send_keys(Name_at_birth)
nationalityAtBirth = web.find_element(By.XPATH, '//*[@id="NationalityAtBirth"]/option[206]')
nationalityAtBirth.click()
countryOfBirth = web.find_element(By.XPATH, '//*[@id="CountryOfBirth"]/option[206]')
countryOfBirth.click()
place_of_birth = web.find_element(By.XPATH, '//*[@id="PlaceOfBirth"]')
place_of_birth.send_keys(Place_of_birth)
actual_nationality = web.find_element(By.XPATH, '//*[@id="NationalityForApplication"]/option[206]')
actual_nationality.click()
date_of_issue_of_passport = web.find_element(By.XPATH, '//*[@id="TraveldocumentDateOfIssue"]')
date_of_issue_of_passport.send_keys(Date_of_issue_of_passport)
passport_valid_until = web.find_element(By.XPATH, '//*[@id="TraveldocumentValidUntil"]')
passport_valid_until.send_keys(Passport_valid_until)
passport_issued_at = web.find_element(By.XPATH, '//*[@id="TraveldocumentIssuingAuthority"]/option[206]')
passport_issued_at.click()

checkBox = web.find_element(By.XPATH, '//*[@id="DSGVOAccepted"]')
checkBox.click()
time.sleep(7)

submit = web.find_element(By.XPATH, '//*[@id="nextButton"]')
submit.click()
time.sleep(1)
web.execute_script('window.print()')
