from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_css_selector("button.btn")
button.click()

window_name = browser.window_handles[1]
browser.switch_to.window(window_name)


num = browser.find_element_by_id("input_value").text
formresult = str(math.log(abs(12 * math.sin(int(num)))))

input1 = browser.find_element_by_tag_name("input")
input1.send_keys(formresult)

button = browser.find_element_by_css_selector("button.btn")
button.click()

print(browser.switch_to.alert.text.split(': ')[-1])

time.sleep(100)

    #   закрыть браузер
browser.quit()

'''
переключение на новую вкалдку 
browser.switch_to.window(window_name)

выбор второй (счет с 0) вкалдки
new_window = browser.window_handles[1]

возврат к текущей вкладке
first_window = browser.window_handles[0]
'''