from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('--headless')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("商品ページURL")

#アカウント情報
email = "Amazon垢のメールアドレス"
password = "Amazon垢のパスワード"

# 購入処理
while True:
    try:
        driver.find_element_by_id("buy-now-button").click()
        sleep(2)
        if driver.title == "Amazonサインイン":
            break
    except:
        driver.refresh()

#ログイン処理
driver.find_element_by_id("ap_email").send_keys(email)
driver.find_element_by_id("continue").click()
driver.find_element_by_id("ap_password").send_keys(password)
driver.find_element_by_id("signInSubmit").click()
sleep(2)

#決済処理
driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div/div[2]/span/span/span/span/input').click()
driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div/span/span/input').click
