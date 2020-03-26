from selenium import webdriver
import time
import math
import re

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    num = browser.find_element_by_id("input_value").text
    formResult = str(math.log(abs(12 * math.sin(int(num)))))

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys(formResult)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    print(browser.switch_to.alert.text.split(': ')[-1])

finally:
    #   ожидание перед закрытием браузера
    time.sleep(10)

    #   закрыть браузер
    browser.quit()

'''
вывод алерта
alert('Hello!');

переключение на окно алерта и принятие
alert = browser.switch_to.alert
alert.accept()

переключение и выбор текста
alert = browser.switch_to.alert
alert_text = alert.text

переключение на окно алетра, но с выбором из двух вариантов
confirm = browser.switch_to.alert
confirm.accept()

отказ в окне-алерте, тоже самое, что нажатие "отмена"
confirm.dismiss()лем ввода текста

окно алерта с доплнительным по
prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()
'''