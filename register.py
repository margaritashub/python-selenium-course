from selenium import webdriver
import time
link = "http://selenium1py.pythonanywhere.com/ru/"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    reg = browser.find_element_by_id("login_link")
    reg.click()
    email = browser.find_element_by_name("registration-email")
    email.send_keys("ab3a@am.rt")
    pas1 = browser.find_element_by_name("registration-password1")
    pas1.send_keys("areallylongpassword1")
    pas2 = browser.find_element_by_name("registration-password2")
    pas2.send_keys("areallylongpassword1")
    submit = browser.find_element_by_name("registration_submit")
    submit.click()
    message = browser.find_element_by_css_selector("div.alertinner")
    assert 'Спасибо за регистрацию!' in message.text
    logout = browser.find_element_by_id("logout_link")
    logout.click()
finally:

    time.sleep(15)

    browser.quit()

