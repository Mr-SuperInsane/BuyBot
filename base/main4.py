# You can use this program on japan. If you wanna use one on other country, you have to make vpn(Internet).
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("amazon product url")
sleep(5)

# Your Amazon's account information
EMAIL = "account email"
PASSWORD = "account password"

while True:
    try:
        driver.find_element(By.ID,'buy-now-button').click()
        sleep(1)
        if driver.title == "Amazonサインイン":
            break
    except:
        driver.refresh()
        sleep(3)

driver.find_element(By.ID, 'ap_email').send_keys(EMAIL)
driver.find_element(By.ID, 'continue').click()
driver.find_element(By.ID, 'ap_password').send_keys(PASSWORD)
driver.find_element(By.ID, 'signInSubmit').click()
print(driver.title)
sleep(2)
driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div[3]/div/div[2]/div[1]/form/div[2]/div/div/div/span/span/input').click()
sleep(3)
if driver.title == "Amazonプライム無料体験をお試しください":
    driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div/div[2]/table/tbody/tr/td/form/div[2]/div/div[1]/div[2]/a').send_keys(Keys.ENTER)
sleep(1)
driver.find_element(By.ID, '/html/body/div[5]/div[1]/div[2]/form/div/div/div/div[2]/div/div[1]/div/div[1]/div/span/span/input').click()