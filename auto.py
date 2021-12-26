from selenium import webdriver
import time

web = webdriver.Chrome()
web.get('https://india-portal.wabco-auto.com/Login.aspx')

time.sleep(2)

vcode = "250042"
vCodeBox = web.find_element_by_id('TextBox1')
vCodeBox.send_keys(vcode)

vpass = "Mapl@1234"
vPassBox = web.find_element_by_id('TextBox2')
vPassBox.send_keys(vpass)

vselect = "Supplier"
vSelectBox = web.find_element_by_id('DropDownList1')
vSelectBox.send_keys(vselect)

web.find_element_by_id('Button1').click()
