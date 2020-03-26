from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

#   импортируется специальный класс Select из библиотеки WebDriver
#   инициализируется новый объект: в него передается WebElement с тегом select

link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    #   взятие исходных значений
    #   по-умолчанию строковое значение взятого элемента
    varNum = browser.find_element_by_id("input_value").text
    varResult = str(math.log(abs(12 * math.sin(int(varNum)))))

    #   находим кнопку на странице
    button = browser.find_element_by_tag_name("button")
    #   скролл хрен знает насколько. но можно попиксельно
    browser.execute_script("window.scrollBy(0, 200);")
    button.click()

    # выбор radiobatton "Robots rule!"
    radiobuttonClick = browser.find_element_by_id("robotsRule")
    radiobuttonClick.click()

    # отметка checkbox "I`m the robot"
    checkboxClick = browser.find_element_by_id("robotCheckbox")
    checkboxClick.click()

    #   находим поле для ввода
    inputNum = browser.find_element_by_id("answer")
    #   вставляем посчитанное значение в поле
    inputNum.send_keys(varResult)
    button.click()

finally:
    #   ожидание перед закрытием браузера
    time.sleep(10)

    #   закрыть браузер
    browser.quit()

