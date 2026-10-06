import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # 1. Ждём, пока цена снизится до $100 (не менее 12 секунд)
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # 2. Нажимаем кнопку "Book"
    browser.find_element(By.ID, "book").click()

    # 3. Решаем математическую задачу
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)

    # 4. Отправляем решение
    browser.find_element(By.ID, "solve").click()

finally:
    # Оставляем время, чтобы скопировать код из всплывающего окна
    time.sleep(30)
    browser.quit()
