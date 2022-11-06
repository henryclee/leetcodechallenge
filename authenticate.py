from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time


#chrome_options = Options()

#chrome_options.add_experimental_option("detach", True)

# , options= chrome_options
def authenticateUser(user, password):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("https://leetcode.com/accounts/login/")
    driver.find_element(By.ID, 'id_login').send_keys(user)
    driver.find_element(By.ID, 'id_password').send_keys(password)
    loginButton = driver.find_element(By.ID, 'signin_btn')

    action = ActionChains(driver)
    action.move_to_element(loginButton).click().perform()

    time.sleep(1)

    WebDriverWait(driver, 10000).until(EC.element_to_be_clickable((By.ID, 'signin_btn'))).click()
    time.sleep(1)
    cookies = driver.get_cookies()
    arr = {}
    for cookie in cookies:
        if cookie["name"] == "LEETCODE_SESSION":
            arr["LEETCODE_SESSION"] = cookie["value"]
        if cookie["name"] == "csrftoken":
            arr["csrftoken"] = cookie["value"]
    return arr

#authenticate("UBHack2022", "TennisBalls123")