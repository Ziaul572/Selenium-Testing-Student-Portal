from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

name = "Ziaul Haque Rafi"
email = "2020-1-60-118@std.ewubd.edu"
password = "1111"
id = "2020-1-60-118"
phone = "01845522620"
dob = "12161999"
address = "38/A South Kazla, Dhaka"
cgpa = 4

def stuAdd(name, email, password, id, phone, dob, address, cgpa):
    driver.get("http://127.0.0.1:5002/")
    driver.maximize_window()
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[@name=\'submit-adm\']").click()
    time.sleep(2)
    driver.find_element(By.NAME, "adm_name").send_keys("admin")
    driver.find_element(By.NAME, "adm_password").send_keys("admin")
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@id=\'btn\']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@id=\'stuSignUp\']").click()
    time.sleep(3)
    driver.find_element(By.NAME, "inputName").send_keys(name)
    time.sleep(1)
    driver.find_element(By.NAME, "inputEmail").send_keys(email)
    time.sleep(1)
    driver.find_element(By.NAME, "inputID").send_keys(id)
    time.sleep(1)
    driver.find_element(By.NAME, "inputPassword").send_keys(password)
    time.sleep(1)
    driver.find_element(By.NAME, "inputConfirmPassword").send_keys(password)
    time.sleep(1)
    driver.find_element(By.NAME, "phone").send_keys(phone)
    time.sleep(1)
    driver.find_element(By.NAME, "selected-department").click()
    time.sleep(2)
    driver.find_element(By.NAME, "selectCSE").click()
    time.sleep(1)
    driver.find_element(By.NAME, "dob").send_keys(dob)
    time.sleep(1)
    driver.find_element(By.NAME, "address").send_keys(address)
    time.sleep(1)
    driver.find_element(By.NAME, "cgpa").send_keys(cgpa)
    time.sleep(1)
    driver.find_element(By.ID, "sub").click()
    print("Student Added Successfully")
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[@id='profile']").click()
    driver.find_element(By.XPATH, "//a[@id='Logout']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@name=\'submit-stu\']").click()
    time.sleep(2)
    driver.find_element(By.NAME, "stu_Id").send_keys(id)
    time.sleep(1)
    driver.find_element(By.NAME, "stu_password").send_keys(password)
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[@id=\'btn\']").click()
    time.sleep(4)
    print("logged In")
stuAdd(name, email, password, id, phone, dob, address, cgpa)