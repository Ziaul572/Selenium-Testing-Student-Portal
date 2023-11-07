from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

testSuiteUsername=['119', '118', '119']
testSuitePassword=['6232', '1', '2']

def test_localhostLogin(username,password,i):


    driver.get("http://127.0.0.1:5002/")
    time.sleep(2)
    #  setWindowSize | 1920x1040 | 
    #driver.set_window_size(1920, 1040)
    # Maximize 
    driver.maximize_window()
    #  click | xpath=(//input[@name='submitButton'])[2] 
    #driver.find_element(By.XPATH, "(//input[@name=\'submitButton\'])[2]").click()
    #  click | xpath=//input[@name='username'] | 
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@name=\'submit-stu\']").click()
    #  type | xpath=//input[@name='username'] | mm
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@name=\'stu_Id\']").send_keys(username)
    #  click | xpath=//input[@name='pwd'] | 
    driver.find_element(By.XPATH, "//input[@name=\'stu_password\']").click()
    #  type | xpath=//input[@name='pwd'] | 123
    driver.find_element(By.XPATH, "//input[@name=\'stu_password\']").send_keys(password)
    #  click | xpath=//input[@name='submitButton'] | 
    driver.find_element(By.XPATH, "//button[@id=\'btn\']").click()
    #wait = WebDriverWait(driver, 3)
    #submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='submitButton']")))
    #driver.find_element(By.NAME, "email").send_keys("2020-1-60-118@std.ewubd.edu")
    time.sleep(2)
    #driver.find_element(By.NAME, "password").click()
    #driver.find_element(By.NAME, "Password").send_keys("11111111")
    # Click the submit button
    #submit_button.click()
    #driver.find_element(By.XPATH, "//input[@name='submitButton']").click()
    
    #driver.find_element(By.XPATH, "//button[@id='submitBtn']").click()
    #driver.find_element(By.NAME, "submitBtn").click()
    

    get_url= driver.current_url
    if(get_url=="http://127.0.0.1:5002/homepage"):
        print("test- "+str(i)+" successfully logged in")
       # driver.find_element(By.XPATH, "/html/body/header/blockquote/form[1]/input").click()
        driver.find_element(By.XPATH, "//button[@id='profile']").click()
        driver.find_element(By.XPATH, "//a[@id='Logout']").click()
    elif(get_url=="http://127.0.0.1:5002"):
        print("test- "+str(i)+" failed to logged in")
    else:
        print("test- "+str(i)+" failed to logged in")
lenofList=len(testSuiteUsername)
for i in range(0,lenofList):
    test_localhostLogin(testSuiteUsername[i],testSuitePassword[i],i+1)