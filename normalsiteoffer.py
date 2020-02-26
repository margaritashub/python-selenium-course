from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = "http://selenium1py.pythonanywhere.com/ru/"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    reg = browser.find_element_by_id("login_link")
    reg.click()
    email = browser.find_element_by_name("login-username")
    email.send_keys("ab3a@am.rt")
    pas1 = browser.find_element_by_name("login-password")
    pas1.send_keys("areallylongpassword1")
    submit = browser.find_element_by_name("login_submit")
    submit.click()
    message = browser.find_element_by_css_selector("div.alertinner")
    assert 'Рады видеть вас снова' in message.text
    browser.find_element_by_link_text("Предложения").click()
    browser.find_element_by_link_text("Coders at Work").click()
    browser.find_element_by_css_selector(".btn-add-to-basket").click()
    assert browser.page_source.find("Codes at work был добавлен в вашу корзину.")

    browser.find_element_by_link_text("Посмотреть корзину").click()
    number = browser.find_element_by_name("form-0-quantity")
    number.clear()
    number.send_keys(3)
    browser.find_element_by_css_selector(".input-group-btn").click()
    assertsave = browser.find_element_by_css_selector("#messages")
    text = "Ваша корзина удовлетворяет условиям предложения Normal site offer."
    assert text in assertsave.text
    browser.find_element_by_link_text("Посмотреть корзину").click()
    number = browser.find_element_by_name("form-0-quantity")
    number.clear()
    number.send_keys(0)
    browser.find_element_by_css_selector(".input-group-btn").click()
    assertsave = browser.find_element_by_css_selector("#messages")
    text = "Ваша корзина теперь пуста"
    assert text in assertsave.text
    logout = browser.find_element_by_id("logout_link")
    logout.click()
finally:

    time.sleep(12)

    browser.quit()
