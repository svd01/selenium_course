from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной

button = WebDriverWait(browser, 15).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "100"))


button = browser.find_element_by_id("book")
button.click()

num = browser.find_element_by_id("input_value").text
formResult = str(math.log(abs(12 * math.sin(int(num)))))

input1 = browser.find_element_by_id("answer")
input1.send_keys(formResult)

button = browser.find_element_by_id("solve")
button.click()

print(browser.switch_to.alert.text.split(': ')[-1])

browser.quit()






