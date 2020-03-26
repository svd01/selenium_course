from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    var1 = browser.find_element_by_id("num1")
    var2 = browser.find_element_by_id("num2")
    #var3 = str(int(var1) + int(var2))
    #varSum = str(int(var1) + int(var2))
    print(var1, type(var1))


    #search = browser.find_element_by_text("%s varSum")
    #print (search)

    browser.find_element_by_tag_name("select").click()
    browser.find_element_by_css_selector("option:nth-child(2)").click() 

finally:
    time.sleep(10)
    browser.quit()
