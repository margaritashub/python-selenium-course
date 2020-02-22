from selenium import webdriver
import time

link = "http://selenium1py.pythonanywhere.com/ru/"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_link_text("Books").click()
    browser.find_element_by_link_text("Hacking Exposed Wireless").click()
    browser.find_element_by_css_selector(".btn-add-to-basket").click()
    message = browser.find_element_by_css_selector("div:nth-child(1)")
    assert  browser.page_source.find("Hacking Exposed Wireless был добавлен в вашу корзину.")
    browser.find_element_by_link_text("Посмотреть корзину").click()
    number = browser.find_element_by_name("form-0-quantity")
    number.clear()
    number.send_keys(0)
    browser.find_element_by_css_selector(".input-group-btn").click()
    browser.find_element_by_css_selector(".alertinner")
    
    assert  browser.page_source.find("Ваша корзина теперь пуста")
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(12)
    # закрываем браузер после всех манипуляций
    browser.quit()
