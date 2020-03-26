from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    #var = str(math.ceil(math.pow(math.pi, math.e)*10000))
    #link = browser.find_element_by_link_text(link)
    #link.click()

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    #button = browser.find_element(By.ID, "submit")
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    #button = browser.find_element(By.CSS_SELECTOR, "button.submit")
    button.click()


finally:
    time.sleep(30)
    browser.quit()

