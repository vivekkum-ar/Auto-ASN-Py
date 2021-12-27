from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException

web = webdriver.Chrome()
web.implicitly_wait(0.5)
web.get('https://india-portal.wabco-auto.com/Login.aspx')

time.sleep(2)

def autoFill(elemId,value):
    web.find_element_by_id(elemId).send_keys(value)

def login(vCode,vPass):
    autoFill("TextBox1",vCode)
    autoFill("TextBox2",vPass)
    autoFill("DropDownList1","Supplier")
    web.find_element_by_id('Button1').click()
    try:
        # define element
        element = web.find_element_by_xpath("/html/body/form/div[4]/div/div[3]/div/div[1]/div/div[2]/div[2]/span")
        web.find_element_by_id("TextBox1").clear()
        web.find_element_by_id("TextBox2").clear()
        print("Wrong password! Please try again")
        login(input("Enter Vendor Code: "),input("Enter Vendor Password: "))        
    except NoSuchElementException as e:
        print("Element Not Found!")


login(input("Enter Vendor Code: "),input("Enter Vendor Password: "))

web.execute_script("javascript:__doPostBack('CreateASN','')")
txt = web.execute_script('return(document.getElementsByTagName("span")[9].innerHTML +" (" + document.getElementsByTagName("span")[10].innerHTML) + ")"')
print("You are logged in as: " + txt)