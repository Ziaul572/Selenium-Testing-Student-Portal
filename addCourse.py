from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

fac_email = "Dr.S.Ripon@ewubd.edu"
fac_password = "123"
code = "CSE430"
cName = "SoftWare Quality and Assurance"
des = "Software Quality Control and Testing"

def addCourse(fac_email, fac_password, c_code, c_name, c_des):
    driver.get("http://127.0.0.1:5002/")
    
    driver.maximize_window()
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[@name=\'submit-fac\']").click()
    time.sleep(1)
    driver.find_element(By.NAME, "fac_email").send_keys(fac_email)
    driver.find_element(By.NAME, "fac_password").send_keys(fac_password)
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@id=\'btn\']").click()
    time.sleep(1)
    #driver.find_element(By.XPATH, "//[@id=\'navbar\']").click()
    driver.find_element(By.ID, "navbar").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@id=\'addCourse\']").click()
    time.sleep(1)
    driver.find_element(By.NAME, "course_code").send_keys(c_code)
    time.sleep(1)
    driver.find_element(By.NAME, "course_name").send_keys(c_name)
    time.sleep(1)
    driver.find_element(By.NAME, "course_description").send_keys(c_des)
    time.sleep(1)
    driver.find_element(By.NAME, "course_seat").click()
    time.sleep(1)
    driver.find_element(By.NAME, "s40").click()
    time.sleep(1)
    driver.find_element(By.NAME, "course_credit").click()
    time.sleep(1)
    driver.find_element(By.NAME, "v4").click()
    time.sleep(1)
    driver.find_element(By.NAME, "btn").click()
    
    #driver.find_element(By.ID, "sub").click()
    time.sleep(5)

addCourse(fac_email, fac_password, code, cName, des)