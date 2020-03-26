from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)


    x_element = browser.find_element_by_css_selector("*[id='input_value']")
    x = x_element.text
    y = calc(x)
 
    print('This is Y:', y)

    input_text = browser.find_element_by_css_selector("*[id='answer']")
    input_text.send_keys(y)
    
    option1 = browser.find_element_by_css_selector("[id='robotCheckbox']")
    option1.click()

    option2 = browser.find_element_by_css_selector("[id='robotsRule']")
    option2.click()
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(50)
    browser.quit()
