from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import os
import time 

link = "http://127.0.0.1:8000/login"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
test_result_path = os.path.join(BASE_DIR, "test_send_2_telegram_result.txt")
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
try:
    # Явное ожидание нахождения вишлиста перед его использованием
    wait = WebDriverWait(browser, 10)
    element = wait.until(EC.presence_of_element_located((By.XPATH, "//h3[contains(text(), 'ТестВишлист')]")))
    element.click()
    time.sleep(3)
    button = browser.find_element(By.CLASS_NAME, "telegram-btn")
    button.click()
    element = browser.find_element(By.XPATH, "//select/option[contains(text(), 'ТестВишлист')]")
    element.click()
    input = browser.find_element(By.NAME, "telegram_username")
    input.clear()
    input.send_keys("@Korneev_N_V")
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()
    time.sleep(3)
    
    # Ждём появления alert и отменяем его
    try:
        wait = WebDriverWait(browser, 5)
        alert = wait.until(EC.alert_is_present())
        print("Alert найден, отменяем...")
        alert.dismiss()
        time.sleep(2)
    except Exception as e:
        print(f"Alert не найден или ошибка: {e}")

    if browser.current_url.startswith("https://t.me/Kornee"):
        print("Мы на нужной странице ✅")
        result = "Сообщение отправлено в Telegram ✅"
    else:
        print("Мы на другой странице ❌")
        result = "Не удалось отправить сообщение ❌"

    time.sleep(2)
    with open(test_result_path, "a", encoding="utf-8") as file:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{current_time} — {result}\n")

    time.sleep(2)

    # теперь возвращаемся на предыдущую страницу (назад)
    browser.back()

    time.sleep(2)

    browser.back()
    
    # Ждём перед удалением
    time.sleep(2)
    # Прокрутка в самый верх
    browser.execute_script("window.scrollTo(0, 0);")
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



except Exception as e:
    result = f"Тест упал с ошибкой: {e}"
    print(result)



finally:
    time.sleep(3)
    os.startfile(test_result_path)
    # закрываем браузер
    browser.quit()
    
    # Логируем результат
    try:
        with open(test_result_path, "a", encoding="utf-8") as file:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{current_time} — {result}\n")
    except:
        pass
