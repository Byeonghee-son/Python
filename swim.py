from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
import threading

def register_for_class(username, password):
    driver = webdriver.Chrome()
    while True:
        try:
            driver.get("https://www.osansports.or.kr/fmcs/45")
            driver.implicitly_wait(2)

            username_elem = driver.find_element(By.ID, 'user_id')
            password_elem = driver.find_element(By.ID, 'user_password')

            username_elem.send_keys(username)
            password_elem.send_keys(password)
            password_elem.send_keys(Keys.RETURN)

            driver.implicitly_wait(2)
            
            #https://www.osansports.or.kr/fmcs/29?subject=%EC%9E%85%EB%AC%B8&action=read&page=1&comcd=OSANSISUL01&classcd=00068&type=R 이게 입문수영 주소
            url = "https://www.osansports.or.kr/fmcs/29?action=read&comcd=OSANSISUL01&classcd=00234&type=R"
            driver.get(url)

            registration_btn = driver.find_element(By.CSS_SELECTOR, 'button.button.action_write')
            registration_btn.click()

            driver.implicitly_wait(1)
            alert = Alert(driver)
            
            if alert.text == "이미 수강신청이 되어 있습니다.":
                print(f"Account {username} is already registered.")
                break
            
            elif "로그아웃이 필요한 메뉴입니다." in alert.text:
                print(f"Account {username} needs to login again.")
                continue

            alert.accept()
            driver.implicitly_wait(1)

            success_element = driver.find_element(By.XPATH, '//strong[text()="수강신청 접수 완료"]')
            if success_element:
                print(f"Account {username} successfully registered!")
                break

            time.sleep(2)
        except Exception as e:
            print(f"Error for account {username}: {e}")
            time.sleep(10)

    driver.quit()

accounts = [
    {"username": "tn414848", "password": "Qwer!234"},
    {"username": "친구분아이디", "password": "친구분비밀번호"}  # 여기에 더 많은 계정을 추가할 수 있습니다.
]

threads = []

for account in accounts:
    thread = threading.Thread(target=register_for_class, args=(account["username"], account["password"]))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
