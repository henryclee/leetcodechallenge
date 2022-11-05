from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



chrome_options = Options()

chrome_options.add_experimental_option("detach", True)


user = "UBHack2022"
password = "TennisBalls123"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options= chrome_options)

driver.get("https://leetcode.com/accounts/login/")
driver.find_element(By.ID, 'id_login').send_keys(user)
driver.find_element(By.ID, 'id_password').send_keys(password)
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable(By.XPATH, '//*[@id="signin_btn"]')).click()


#driver.find_element(By.ID, "signin_btn").click()
print("good")

"""element = WebDriverWait(driver, 20).until(
EC.presence_of_element_located((By.ID, "signin_btn")))# click login button
element.click()"""