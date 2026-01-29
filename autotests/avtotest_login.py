from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import os
import time 

link = "http://127.0.0.1:8000/login"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
test_result_path = os.path.join(BASE_DIR, "test_login_result.txt")
try:
    browser = webdriver.Chrome()
    browser.get(link)

    def trying_login(email, password, defenition):
        try:
            input1 = browser.find_element(By.ID, "email")
            input1.clear()
            input1.send_keys(email)
            input2 = browser.find_element(By.ID, "password")
            input2.clear()
            input2.send_keys(password)
            button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
            button.click()

            time.sleep(2)

            if browser.current_url == "http://127.0.0.1:8000/wishlist":
                result = "Вход выполнен"
                print("Вход выполнен")
            else:
                result = "Вход не выполнен"
                print("Вход не выполнен")
            

        except Exception as e:
            result = f"Тест упал с ошибкой: {e}"
            print(result)
        
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
