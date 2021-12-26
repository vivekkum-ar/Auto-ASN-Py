from selenium import webdriver
import time

web = webdriver.Chrome()
web.get('https://india-portal.wabco-auto.com/Login.aspx')

time.sleep(2)

def autoFill(eleId,vale):
    web.find_element_by_id(eleId).send_keys(vale)


autoFill("TextBox1","250042")
autoFill("TextBox2","Mapl@1234")
autoFill("DropDownList1","Supplier")
web.find_element_by_id('Button1').click()
