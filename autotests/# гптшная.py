# гптшная
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import os
import time 

link = "http://127.0.0.1:8000/login"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
test_result_path = os.path.join(BASE_DIR, "test_login_result.txt")
bg = None
try:
    browser = webdriver.Chrome()
    browser.get(link)

    def trying_login(email, password, defenition):
        wait = WebDriverWait(browser, 7)

        try:
            # --- Ввод email ---
            email_input = wait.until(
                EC.presence_of_element_located((By.ID, "email"))
            )
            email_input.clear()
            email_input.send_keys(email)

            # --- Ввод пароля ---
            password_input = browser.find_element(By.ID, "password")
            password_input.clear()
            password_input.send_keys(password)

            # --- Клик по кнопке ---
            browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

            # --- Проверка результата логина ---
            try:
                wait.until(EC.url_contains("/wishlist"))
                login_success = True
            except TimeoutException:
                login_success = False

            # --- Если логин успешен ---
            if login_success:
                result = "Вход выполнен"

                # Ждём картинку
                img = wait.until(
                    EC.presence_of_element_located((By.ID, "cornerPlant"))
                )

                # Проверяем, что картинка реально загрузилась
                bg = browser.find_element(By.ID, "cornerPlant") \
            .value_of_css_property("background-image")

            if bg != "none":
                print("Фоновая картинка загружена ✅")
                result += " | Картинка загрузилась ✅"

            else:
                    result += " | Картинка НЕ загрузилась ❌"


        except Exception as e:
            result = f"Тест упал с ошибкой: {e}"

        # --- Логирование результата ---
        with open(test_result_path, "a", encoding="utf-8") as file:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{current_time} — {defenition} — {result}\n")

        print(result)
        return result
    test_data = [
        ("", "", "пустые поля"),
        ("wrong@mail.ru", "Frenz5329", "неверный email"),
        ("iluykol@mail.ru", "wrongpass", "неверный пароль"),
        ("test@test.com", "test", "корректные данные")
    ]

    for email, password, defenition in test_data:
        print(f"Пробуем логин: {email}")
        trying_login(email, password, defenition)

finally:
    time.sleep(3)
    # закрываем браузер
    browser.quit()
    
 
    os.startfile(test_result_path)

