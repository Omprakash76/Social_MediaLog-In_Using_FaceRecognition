#!/usr/bin/env python
# coding: utf-8
print("Welcome to Facebook")
from selenium import webdriver
from getpass import getpass
from time import sleep

use = "Write your Email/Mobile number Here"
pwd = "write Your Password Here"
message=input('\nEnter your message for status:')

print("\nOpening Facebook...")

browser = webdriver.Chrome("/home/omprakash/chromedriver_linux64/chromedriver")
browser.get('https://www.facebook.com/login')

print("\nWelcome to Facebook")
print("\nLogging in...")

username_box = browser.find_element_by_id('email')
username_box.send_keys(use)
print("\nEmail/Mobile number entered...")
sleep(1)

pwd_box=browser.find_element_by_id('pass')
pwd_box.send_keys(pwd)
print("\nPassword entered...")
sleep(2)

fb_login=browser.find_element_by_id('loginbutton')
fb_login.submit()
sleep(3)
print("Loged in Successfully!!!")

status= browser.find_element_by_xpath("//textarea[@name='xhpc_message']")
status.send_keys(message);
print("Status trying")
sleep(2)

postbutton = browser.find_element_by_xpath("//button[contains(.,'Share')]")
postbutton.click()
print("post done")
