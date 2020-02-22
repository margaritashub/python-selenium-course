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
    acc = browser.find_element_by_css_selector('.icon-user')
    acc.click()
    abook = browser.find_element_by_link_text("Адресная книга")
    abook.click()
    addad = browser.find_element_by_link_text("Добавить новый адрес")
    addad.click()
    select = Select(browser.find_element_by_id("id_title"))
    select.select_by_value("Miss")
    name = browser.find_element_by_name("first_name")
    name.send_keys("Rita")
    sname = browser.find_element_by_name("last_name")
    sname.send_keys("Nerita")
    line1 = browser.find_element_by_id("id_line1")
    line1.send_keys("ROSSIYA")
    line2 = browser.find_element_by_id("id_line2")
    line2.send_keys("BOLWAYA")
    line4 = browser.find_element_by_name("line4")
    line4.send_keys("NIJNYAYA PAVLOVKA")
    state = browser.find_element_by_name("state")
    state.send_keys("derevnya")
    pstcode = browser.find_element_by_name("postcode")
    pstcode.send_keys("44444444")
    select2 = browser.find_element_by_name("country")

    browser.execute_script("return arguments[0].scrollIntoView(true);", select2)
    select2.select_by_visible_text("Russian Federation")

    save = browser.find_element_by_css_selector('.btn-lg')
    save.click()

    assertsave = browser.find_element_by_css_selector("div.alertinner")
    assert "добавлен" in assertsave.text
    logout = browser.find_element_by_id("logout_link")
    logout.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(11)
    # закрываем браузер после всех манипуляций
    browser.quit()