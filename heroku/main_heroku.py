# You can use this program on japan. If you wanna use one on other country, you have to make vpn(Internet).
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options, executable_path='/app/.chromedriver/bin/chromedriver')
driver.get("Amazon url")
sleep(5)

# Your Amazon's account
email = "your email"
password = "your password"

while True:
    try:
        driver.find_element_by_id("buy-now-button").click()
        sleep(1)
        if driver.title == "Amazonサインイン":
            break
    except:
        driver.refresh()
        sleep(3)

driver.find_element_by_id("ap_email").send_keys(email)
driver.find_element_by_id("continue").click()
driver.find_element_by_id("ap_password").send_keys(password)
driver.find_element_by_id("signInSubmit").click()
sleep(2)
driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div[3]/div/div[2]/div[1]/form/div[2]/div/div/div/span/span/input").click()
sleep(3)
if driver.title == "Amazonプライム無料体験をお試しください":
    driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div[2]/table/tbody/tr/td/form/div[2]/div/div[1]/div[2]/a").send_keys(Keys.ENTER)
sleep(1)
driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[2]/form/div/div/div/div[2]/div/div[1]/div/div[1]/div/span/span/input").click()

# Heroku Buildpacks (before deploy)
# https://github.com/heroku/heroku-buildpack-chromedriver.git
# https://github.com/heroku/heroku-buildpack-google-chrome.git

# Heroku Deploy (cmd)
# first:Heroku CLI install 
# cmd:heroku login
# cmd:heroku create project_name
# cmd:git init (on this folder)
# cmd:git add.
# cmd:git remote add heroku https:// (when you create heroku project, you can get https://~~~)
# cmd:git commit -m "commit name"
# cmd:git push heroku master

# finish deploy
