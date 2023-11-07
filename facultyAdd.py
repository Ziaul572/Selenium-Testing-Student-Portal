from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

name = "Dr Shamin Ripon"
email = "Dr.S.Ripon@ewubd.edu"
password = "123"


def facAdd(name, email, password):
    driver.get("http://127.0.0.1:5002/")
    
    driver.maximize_window()
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[@name=\'submit-adm\']").click()
    time.sleep(1)
    driver.find_element(By.NAME, "adm_name").send_keys("admin")
    time.sleep(1)
    driver.find_element(By.NAME, "adm_password").send_keys("admin")
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[@id=\'btn\']").click()
    time.sleep(1)
    
    driver.find_element(By.XPATH, "//a[@id=\'facSignUp\']").click()
    time.sleep(1)
    driver.find_element(By.NAME, "inputName").send_keys(name)
    time.sleep(1)
    driver.find_element(By.NAME, "inputEmail").send_keys(email)
    time.sleep(1)
    driver.find_element(By.NAME, "inputPassword").send_keys(password)
    time.sleep(1)
    driver.find_element(By.NAME, "inputConfirmPassword").send_keys(password)
    time.sleep(1)
    driver.find_element(By.ID, "sub").click()
    time.sleep(5)

facAdd(name, email, password)