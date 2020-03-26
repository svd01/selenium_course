from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    inputFirst_name = browser.find_element_by_name("firstname")
    inputFirst_name.send_keys("Valentin")

    inputLast_name = browser.find_element_by_name("lastname")
    inputLast_name.send_keys("Serednev")

    inputEmail = browser.find_element_by_name("email")
    inputEmail.send_keys("bloood1991@mail.ru")

    #   получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    #   добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'file_test_2.2.txt')

    #   ищем кнопку "Добавить файл"
    inputFile = browser.find_element_by_id("file")
    inputFile.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    #   ожидание перед закрытием браузера
    time.sleep(10)

    #   закрыть браузер
    browser.quit()

