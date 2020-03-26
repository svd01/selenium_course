from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
#   импортируется специальный класс Select из библиотеки WebDriver
#   инициализируется новый объект: в него передается WebElement с тегом select

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    #   взятие исходных значений
    #   по-умолчанию строковое значение взятого элемента
    varNum1 = browser.find_element_by_id("num1").text
    varNum2 = browser.find_element_by_id("num2").text
    varSum = str(int(varNum1) + int(varNum2))

    # ввод итогового числа в поле
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(varSum)  # ищем элемент с текстом "Python

    #select = Select(browser.find_element_by_tag_name("select"))
    # активация "Submit"
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:

    time.sleep(4)

    # закрыть браузер
    browser.quit()

