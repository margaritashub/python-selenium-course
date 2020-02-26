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
    def findabook():
         browser.find_element_by_link_text("Books").click()
         browser.find_element_by_link_text("Hacking Exposed Wireless").click()
    findabook()
    browser.find_element_by_id("write_review").click()
    browser.find_element_by_id("id_title").send_keys("OCHEN HOROWO")
    text = "tolko ne rabotaet"
    browser.find_element_by_id("id_body").send_keys(text)
    star = browser.find_element_by_css_selector(".star-rating:nth-child(5)")
    star.click()
    browser.find_element_by_css_selector('#add_review_form button').click()
    message = browser.find_element_by_css_selector("div.alertinner")
    assert 'Ваш отзыв добавлен' in message.text
    findabook()
    reviews = browser.find_element_by_id("reviews")
    assert text in reviews.text
    logout = browser.find_element_by_id("logout_link")
    logout.click()
finally:

    time.sleep(12)

    browser.quit()