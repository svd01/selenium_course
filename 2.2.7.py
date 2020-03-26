from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # поиск изображения
    imageBack = browser.find_element_by_id("treasure")    
    
    # взятие у элемента imageBack значение value
    imageIn = imageBack.get_attribute("valuex")
    print(imageIn)
    
    # рассчет функции
    pi = str(math.log(abs(12*math.sin(int(imageIn)))))
    print(pi)
    
    # ввод ответа в поле
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys(pi)
    
    # отметка checkbox "I`m the robot"
    checkboxClick = browser.find_element_by_id("robotCheckbox")
    checkboxClick.click()
    
    # выбор radiobatton "Robots rule!"
    radiobuttonClick = browser.find_element_by_id("robotsRule")
    radiobuttonClick.click()
    
    # активация "Submit"
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:

    time.sleep(30)
    
    # закрыть браузер
    browser.quit()

