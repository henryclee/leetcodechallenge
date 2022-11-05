import requests
import mechanize
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

"""
# Fill in your details here to be posted to the login form.
payload = {
    'id_login': '',
    'id_password': ''
}

header = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}


# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    heads = s.get('https://leetcode.com/accounts/login/').headers
    p = s.post('https://leetcode.com/accounts/login/', data=payload)
    # print the html returned or something more intelligent to see if it's a successful login page.
    print(p.text)
"""
user = "UBHack2022"
password = "TennisBalls123"
driver = webdriver.Chrome("C:/Users/Morgan Li/Downloads/chromedriver_win3")
driver.get("https://leetcode.com/accounts/login/")
# find username/email field and send the username itself to the input field
driver.find_element(By.ID, 'login').send_keys(user)
#password_form = driver.find_element(By.ID, 'password')

# find password input field and insert password as well
driver.find_element(By.ID, 'password').send_keys(password)
# click login button
driver.find_element(By.ID, "signin_btn").click()
