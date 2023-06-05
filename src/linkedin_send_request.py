# This script is having errors 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from configparser import ConfigParser
from selenium.webdriver.chrome.service import Service

# Put your email and password for linkein in config.ini file 
EMAIL = 'EMAIL'
PASSWORD = 'PASSWORD'

CONNECTION_LIMIT = 10
# You can set here how many connections you want to send request

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36")

# Set the path to the Chrome driver executable
chromedriver_path = 'C:/Users/kgn27/AppData/Local/pyppeteer/pyppeteer/local-chromium/588429/chrome-win32/chromedriver.exe'

# Configure the Chrome options
options = webdriver.ChromeOptions()
options.add_argument('--disable-gpu')  # Disable GPU acceleration

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=Service(chromedriver_path), options=options)

driver.get("https://www.linkedin.com/login")

action = ActionChains(driver)
driver.implicitly_wait(10)
email = driver.find_element(By.XPATH, "//input[@id='username']")
email.send_keys(EMAIL)
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(PASSWORD)

submit = driver.find_element(By.XPATH, "//button[@aria-label='Sign in']")
submit.click()

width = 540
height = 720
driver.set_window_size(width, height)
profile_url = 'https://www.linkedin.com/in/abhijit-gunjewar-36804059/'
driver.get(profile_url)
driver.implicitly_wait(5)

##############################

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    # Your code for navigating to the profile and interacting with buttons
    
    # Find and click the "Connect" button
    connect_button = driver.find_element(By.XPATH, '//button[contains(@aria-label,"Invite")]')
    # connect_button.click()
    driver.execute_script("arguments[0].click();", connect_button)
    driver.implicitly_wait(10)

    # click on add note
    add_note = driver.find_element(By.XPATH, '//button[contains(@aria-label, "Add a note")]')
    # add_note.click()
    driver.execute_script("arguments[0].click();", add_note)
    driver.implicitly_wait(10)

    # add note
    custom_message = driver.find_element(By.XPATH, "//textarea[@id='custom-message')]")
    custom_message.send_keys("Hi")
    driver.implicitly_wait(10)

    # Find and click the "Send now" button
    send_button = driver.find_element(By.XPATH, '//button[contains(@aria-label, "Send now")]')
    send_button.click()
    driver.implicitly_wait(10)

    # Your code for any additional interactions or steps
    
    print("Success: Connection request sent!")
    
except Exception as e:
    print(f"Error occurred: {str(e)}")

finally:
    # Close the browser window
    driver.quit()
