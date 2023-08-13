from selenium.webdriver import Firefox
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from time import sleep
import os

opts = FirefoxOptions()
opts.binary = FirefoxBinary("/usr/local/bin/firefox")
opts.add_argument("--headless")


class MedbookProcessor:
    def __init__(self):
        self.driver = Firefox(options=opts)
        self.driver.implicitly_wait(2)  # seconds
        self.driver.get("https://www.medbook.com/nl/login")
        self.user_field = self.driver.find_element(By.ID, "Username")
        self.psswd_field = self.driver.find_element(By.ID, "Password")
        self.login_form = self.driver.find_element(By.ID, "login-form")
        self.user_field.send_keys(os.environ.get("USER"))
        self.psswd_field.send_keys(os.environ["MEDBOOK_PW"])
        self.login_form.submit()
        sleep(2)
        self.driver.find_element(
            By.CSS_SELECTOR, "#header #main-menu ul li a.icon-menuitem.logbook"
        ).click()
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "a.button > span").click()
        sleep(2)

    def upload_case(self, date_of_birth, specialty, procedure):
        try:
            self.date_box = self.driver.find_element(
                By.NAME, "log_ingreep_chirurg_patient_geboortedatum"
            )
            self.date_box.clear()
            self.date_box.send_keys(date_of_birth)
            self.specialty_box = Select(
                self.driver.find_element(By.NAME, "log_ingreep_specialiteit-anesthesie")
            )
            self.specialty_box.select_by_value(specialty)
            self.procedure_box = self.driver.find_element(
                By.ID, "log_ingreep_chirurg_andere_specialiteit"
            )
            self.procedure_box.clear()
            self.procedure_box.send_keys(procedure)
            self.supervision_box = self.driver.find_element(
                By.CSS_SELECTOR, "input[type='radio'][value='Z']"
            ).click()
        finally:
            self.driver.find_element(By.NAME, "bewaar_kopier").click()
            sleep(1)
            # driver.close()
            pass
