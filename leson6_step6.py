from selenium import webdriver
import math
link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    var = str(math.ceil(math.pow(math.pi, math.e)*1000))
    button = browser(var)
    button.click()


