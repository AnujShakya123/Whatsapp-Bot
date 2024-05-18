import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

phone = "9997013903"
message = 'Hi there, I have created a whatsapp Automation'

options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
prefs = {"download.default_directory": "."}
options.add_experimental_option("prefs", prefs)
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

BASE_URL = "https://web.whatsapp.com/"
CHAT_URL = "https://web.whatsapp.com/send?phone={phone}&text&type=phone_number&app_absent=1"

browser.get(BASE_URL)
print("Kindly go to output tab and login before the timeout of 240 seconds.")
# Wait for the learner to log in
try:
    wait = WebDriverWait(browser, 240)  # Adjust the timeout value as needed (e.g., 60 seconds)
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true']")))
    print("Logged in successfully. Proceeding to send message")
except Exception as e:
    print("Timeout: Learner did not log in within the specified time.")
    browser.quit()


browser.get(CHAT_URL.format(phone=phone))
time.sleep(20)
try:
    wait = WebDriverWait(browser, 120)  # Adjust the timeout value as needed (e.g., 60 seconds)
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')))
    inp_xpath = ('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
    input_box = WebDriverWait(browser, 90).until(expected_conditions.presence_of_element_located((By.XPATH, inp_xpath)))
    input_box.send_keys(message)
    input_box.send_keys(Keys.ENTER)
    time.sleep(20)
except Exception as e:
    print("Kindly Enter the valid number.")
    browser.quit()








