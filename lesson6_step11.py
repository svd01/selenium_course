from selenium import webdriver
import time
from selenium.webdriver.common.by import By

try: 
    link = "http://suninjuly.github.io/registration2.html"
    #link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

# //input[@placeholder='Input your name'] - уникальный поиск
# (//input[@class='form-control first'])[1] - выбор первого из нескольких (счет с 1)

# Ваш код, который заполняет обязательные поля
    

    input1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your name']")
    input1.send_keys("Name")
    
    input2 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
    input2.send_keys("email")
    
    input3 = browser.find_element(By.XPATH, "//input[@placeholder='Input your phone']")
    input3.send_keys("phone")
    
    #input2 = browser.find_element_by_name("last_name")
    #input2.send_keys("Petrov")
    #input3 = browser.find_element_by_class_name("form-control.city")
    #input3.send_keys("Smolensk")
    #input4 = browser.find_element_by_id("country")
    #input4.send_keys("Russia")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(15)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
