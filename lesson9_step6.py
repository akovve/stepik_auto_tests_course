import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    # 1. Нажимаем кнопку, которая открывает новую вкладку
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # 2. Переключаемся на новую вкладку
    #    Сохраняем список всех открытых вкладок
    window_handles = browser.window_handles
    #    Переключаемся на последнюю (вторую) вкладку
    browser.switch_to.window(window_handles[1])

    # 3. Решаем капчу на новой вкладке
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)

    # 4. Нажимаем кнопку Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    # Оставляем время, чтобы скопировать код из всплывающего окна
    time.sleep(30)
    browser.quit()
