# УЛЬТРААВТОТЕСТ
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import os
import time 

link = "http://127.0.0.1:8000/login"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
test_result_path = os.path.join(BASE_DIR, "all_tests.txt")
try:
    browser = webdriver.Chrome()
    browser.get(link)

    def trying_login(email, password, defenition):
        try:
            input1 = browser.find_element(By.ID, "email")
            wait = WebDriverWait(browser, 5)
            input1.clear()
            wait = WebDriverWait(browser, 5)
            input1.send_keys(email)
            time.sleep(1)
            input2 = browser.find_element(By.ID, "password")
            wait = WebDriverWait(browser, 5)
            input2.clear()
            wait = WebDriverWait(browser, 5)
            input2.send_keys(password)
            time.sleep(1)
            button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
            wait = WebDriverWait(browser, 5)
            button.click()
            time.sleep(1)

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
        ("iluykol@mail.ru", "wroфывфыngpass", "неверный пароль"),
        ("test@test.com", "test", "корректные данные")
    ]

    for email, password, defenition in test_data:
        print(f"Пробуем логин: {email}")
        trying_login(email, password, defenition)

# Ждём загрузки формы создания вишлиста
    
    wait = WebDriverWait(browser, 3)
    input1 = wait.until(EC.presence_of_element_located((By.NAME, "title")))
    input1.clear()
    input1.send_keys("ТестВишлист")
    input2 = browser.find_element(By.NAME, "description")
    input2.clear()
    input2.send_keys("описание тестового вишлиста")
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()
    time.sleep(1)


# ищем созданную карточку вишлиста с использованием WebDriverWait
    wait = WebDriverWait(browser, 7)
    try:
        element = wait.until(EC.presence_of_element_located((By.XPATH, "//h3[contains(text(), 'ТестВишлист')]")))
        result = "вишлист создан"
        print(result)
    except:
        result = "вишлист не создан"
        print(result)
    with open(test_result_path, "a", encoding="utf-8") as file:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{current_time} — {result}\n")

    # Ждём загрузки страницы после создания
    wait = WebDriverWait(browser, 7)
    try:
        # Явное ожидание нахождения вишлиста перед его использованием
        wait = WebDriverWait(browser, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, "//h3[contains(text(), 'ТестВишлист')]")))
        element.click()
# 
        input3 = browser.find_element(By.NAME, "title")
        input3.clear()
        input3.send_keys("Мороженое")
        input4 = browser.find_element(By.NAME, "url")
        input4.clear()
        input4.send_keys("https://market.yandex.ru/card/morozhenoye-slivochnoye-iz-lavki-chay-s-bergamotom/4481099500?do-waremd5=Og53e0zJXKH9RX-NGjHraw&cpc=zYyK3fgeerZZkqca7dY9LChTjO9bdLRfepvA82DZleWHCNdbHtoRb2qz_4CvcfnJopZsPo03uqaTK-ZefLLE8laJiMJHgiPDgs2DZr0gnqXjhL4WTctshGlMAXN1p7oG_fmmVCiZQTae0h8Mtyak4xBRKPA4gLrYoioY1BOksZzboUsUI2fXk3pX1QF4ik6bGzdeecrcL5zqU5L_xPphmEMDxzAkvR84GpcfP1LopXQ4-JW1BiOLfAGeO31lSwqCtSq_ZDY3UcO-KHugmN1cgeE-Ez9QWvMD0TPxtTRqnWjz6zUxN3u4nQQbuiKyKDU2ZEr4YCeN3Sd6mXobvddioiOwmlpQXCiXwT-5fIy1DKS-JI1EWaraFrd0RuxWAg3xFTln2p-meJTVi3XJa2UpLRf_f2Pou5N-qPXW-4PqhydP9_vrrqeAi4Fn-NhHhNMUxSv40UZPwpHE2ttACv3mcZ7G_t7uFN2FZnBtnHvTdD4nun1ncuAlK7p1v9Uocy8n0RhZ1OTWyhqQ1Ge1XFtEvEXhsjbTdodr0c_le__ex0iE6_FhfmnD9bFBDd02VjUnW_gJo2Yu8uY26-kPSSFB3p_qDVMKIFttAKLOWBsMUEI9bcDHFVQvhKWR93Ki1HJPrK97ZYDIMlzz3_nqXM_brX3iJTflcHdZPl_Z3fhzcFFpkQ66l7IPX7h2kH8mvl9duap1axA1VqI%2C&cc=CiA4MzFkZTkyMmZlZGNlZGRiODczMTAzMjgyNDg0ZGYzYxAHgH3m7QY%2C&resale_goods=resale_new&hid=60883585&nid=60883586&show-uid=17689194448569501113206087&showUid=17689194448569501113206087&from-show-uid=17689194448569501113206087&cpa=1&from=search")

        wait = WebDriverWait(browser, 7)
        button = browser.find_element(By.CLASS_NAME, "telegram-btn")
        button.click()
        wait = WebDriverWait(browser, 7)
        element = browser.find_element(By.XPATH, "//select/option[contains(text(), 'ТестВишлист')]")
        element.click()
        input5 = browser.find_element(By.NAME, "telegram_username")
        input5.clear()
        input5.send_keys("@Korneev_N_V")
        button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
        button.click()
        time.sleep(1)
        
        # Ждём появления alert и отменяем его
        try:
            wait = WebDriverWait(browser, 5)
            alert = browser.switch_to.alert
            alert.dismiss()
            time.sleep(1)
            # alert = wait.until(EC.alert_is_present())
            # print("Alert найден, отменяем...")
            # alert.dismiss()
            # wait = WebDriverWait(browser, 7)
        except Exception as e:
            print(f"Alert не найден или ошибка: {e}")

        if browser.current_url.startswith("https://t.me/Kornee"):
            print("Мы на нужной странице ✅")
            result = "Сообщение отправлено в Telegram ✅"
        else:
            print("Мы на другой странице ❌")
            result = "Не удалось отправить сообщение ❌"

        wait = WebDriverWait(browser, 5)
        with open(test_result_path, "a", encoding="utf-8") as file:
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"{current_time} — {result}\n")

        wait = WebDriverWait(browser, 5)

        # теперь возвращаемся на предыдущую страницу (назад)
        browser.back()

        time.sleep(1)

        browser.back()
        
        # Ждём перед удалением
        time.sleep(1)
        # Прокрутка в самый верх
        browser.execute_script("window.scrollTo(0, 0);")
        button = browser.find_element(By.CLASS_NAME, "delete-btn")
        button.click()
        time.sleep(1)

        # Работаем с alert
        alert = browser.switch_to.alert

        # Подтверждаем удаление
        alert.accept()
        # или для отмены
        # alert.dismiss()

        time.sleep(1)
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


    with open(test_result_path, "a", encoding="utf-8") as file:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{current_time} — {result}\n")


finally:
    wait = WebDriverWait(browser, 5)
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

