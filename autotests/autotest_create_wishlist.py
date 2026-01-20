from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import os
import time 

link = "http://127.0.0.1:8000/login"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
test_result_path = os.path.join(BASE_DIR, "test_create_wishlist_result.txt")
#НИЖЕ НЕОБХОДИМО ВВЕСТИ ТЕСТОВЫЙ ЛОГИН И ПАРОЛЬ:
# ТЕСТОВЫЙ ЛОГИН: test@test.com
# ТЕСТОВЫЙ ПАРОЛЬ: test
browser = webdriver.Chrome()
browser.get(link)
input1 = browser.find_element(By.ID, "email")
input1.clear()
input1.send_keys("test@test.com")
input2 = browser.find_element(By.ID, "password")
input2.clear()
input2.send_keys("test")
button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
button.click()

# Ждём загрузки формы создания вишлиста
time.sleep(3)

try:
    wait = WebDriverWait(browser, 3)
    input1 = wait.until(EC.presence_of_element_located((By.NAME, "title")))
    input1.clear()
    input1.send_keys("ТестВишлист")
    input2 = browser.find_element(By.NAME, "description")
    input2.clear()
    input2.send_keys("описание тестового вишлиста")
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

    # Ждём загрузки страницы после создания
    time.sleep(5)

    # ищем созданную карточку вишлиста с использованием WebDriverWait
    wait = WebDriverWait(browser, 7)
    try:
        element = wait.until(EC.presence_of_element_located((By.XPATH, "//h3[contains(text(), 'ТестВишлист')]")))
        result = "вишлист создан"
        print(result)
    except:
        result = "вишлист не создан"
        print(result)
        raise
    with open(test_result_path, "a", encoding="utf-8") as file:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{current_time} — {result}\n")

    # Ждём перед удалением
    time.sleep(2)
    element = browser.find_element(By.XPATH, "//h3[contains(text(), 'ТестВишлист')]")
    element.click()
    time.sleep(3)

    button = browser.find_element(By.CLASS_NAME, "delete-btn")
    button.click()
    time.sleep(2)

    # Работаем с alert
    alert = browser.switch_to.alert

    # Подтверждаем удаление
    alert.accept()
    # или для отмены
    # alert.dismiss()

    time.sleep(5)

    if browser.current_url == "http://127.0.0.1:8000/wishlist":
        try:
            browser.find_element(By.XPATH, "//h3[contains(text(), 'ТестВишлист')]")
            result = "вишлист не удален"
        except:
            result = "вишлист удален"
    else:
        result = "вишлист не удален"

except Exception as e:
    result = f"Тест упал с ошибкой: {e}"
    print(result)

finally:
    with open(test_result_path, "a", encoding="utf-8") as file:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{current_time} — {result}\n")
    
    os.startfile(test_result_path)
    print(result)
    time.sleep(2)
    browser.quit()