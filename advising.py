from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

id = "2020-1-60-118"
password = "1111"

def advising(stu_id, stu_password):
    driver.get("http://127.0.0.1:5002/")
    
    driver.maximize_window()
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[@name=\'submit-stu\']").click()
    time.sleep(1)
    driver.find_element(By.NAME, "stu_Id").send_keys(stu_id)
    time.sleep(1)
    driver.find_element(By.NAME, "stu_password").send_keys(stu_password)
    time.sleep(1)
    
    driver.find_element(By.XPATH, "//button[@id=\'btn\']").click()
    time.sleep(1)
    #driver.find_element(By.XPATH, "//[@id=\'navbar\']").click()
    driver.find_element(By.ID, "navbar").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[@id=\'advising\']").click()
    
    time.sleep(3)
    driver.find_element(By.NAME, "submit-row").click()
    #driver.find_element(By.XPATH, "//button[@name=\'submit-row\']").click()
    #driver.find_element(By.ID, "sub").click()
    time.sleep(5)
    driver.find_element(By.NAME, "drop-row").click()
    #driver.find_element(By.XPATH, "//button[@name=\'drop-row\']").click()
    time.sleep(10)

advising(id , password)