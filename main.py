from selenium import webdriver

driver = webdriver.Chrome("chromedriver.exe")
driver.get("商品ページ")

#アカウント情報
email = "Amazon垢のメールアドレス"
password = "Amazon垢のパスワード"

# 購入処理
while True:
    try:
        driver.find_element_by_id("buy-now-button").click()
        if driver.title == "Amazonサインイン":
            break
    except:
        driver.refresh()

#ログイン処理
driver.find_element_by_id("ap_email").send_keys(email)
driver.find_element_by_id("continue").click()
driver.find_element_by_id("ap_password").send_keys(password)
driver.find_element_by_id("signInSubmit").click()
