import selenium
from selenium import webdriver
from getpass import getpass
from time import sleep

print("Welcome to Linkdin)
use = "8559931989"
pwd = "Om@123456"
message=input('\nEnter your message for status:')

print("Opening Linkdin...\nLogging in...")


browser = webdriver.Chrome('/home/omprakash/chromedriver_linux64/chromedriver')
browser.get('https://in.linkedin.com/')
print("Welcome to Linkdin")
print("\nLogging in...")

username_box = browser.find_element_by_id('login-email')
username_box.send_keys(use)
print("Email entered...")
#sleep(3)


pwd_box=browser.find_element_by_id('login-password')
pwd_box.send_keys(pwd)
print("Password entered...")
#sleep(3)


fb_login=browser.find_element_by_id('login-submit')
fb_login.submit()
print("Linkdin opened!!!")

#if message =="":
#    pass

#else:
#    status= driver.find_element_by_xpath("//textarea[@name='xhpc_message']")
#    status.send_keys(message);
#    print("Status trying")
#    postbutton = driver.find_element_by_xpath("//button[contains(.,'Post')]")
#    postbutton.click()
#print("post done")
sleep(3)

