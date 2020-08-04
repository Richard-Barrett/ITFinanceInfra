#!/usr/bin/python 
# ===========================================================
# Created By: Richard Barrett
# Organization: ITInfra
# Department: Automation
# Purpose: Data PUT Automation
# Date: 08/03/2020
# ===========================================================

import selenium
import shutil
import xlsxwriter
import os
import unittest
import requests
import subprocess
import getpass
import platform
import logging
import time 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
from datetime import date

decrypt = "gpg --output secrets_test.json --decrypt secrets.gpg" 

if os.path.exists("secrets.gpg"):
      returned_value = subprocess.call(decrypt, shell=True)
else:
        print("The file does not exist")
            
import json
with open('information.json','r') as f:
      config = json.load(f)

# Definitions
# find_elements_by_name
# find_elements_by_xpath
# find_elements_by_link_text
# find_elements_by_partial_link_text
# find_elements_by_tag_name
# find_elements_by_class_name
# find_elements_by_css_selector

# System Variables
today = date.today()
date = today.strftime("%m/%d/%Y")
node = platform.node()
system = platform.system()
username = getpass.getuser()
version = platform.version()
current_directory = os.getcwd()

# Check for Version of Chrome

# Options 
#options = webdriver.ChromeOptions() 
#options.add_argument("download.default_directory=current_directory", "--headless")

# WebDriver Path for System
if platform.system() == ('Windows'):
    browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")
elif platform.system() == ('Linux'):
    browser = webdriver.Chrome(executable_path='/home/rbarrett/Drivers/Google/Chrome/chromedriver_linux64/chromedriver')
elif platform.system() == ('Darwin'):
    browser = webdriver(executable_path='~/Drivers/Google/Chrome/chromedriver_mac64/chromedriver')
else:
    print("Are you sure you have the Selenium Webdriver installed in the correct path?")
      
# Parent URL
browser.get("https://invoice-generator.com/#/3")

# If Login
# Credentials NEEDS UNIT TEST
#username = browser.find_element_by_id("login")
#password = browser.find_element_by_id("password")
#username.send_keys(config['user']['name'])
#password.send_keys(config['user']['password'])

# Invoice Number

# Put Date

# PUT Invoice From  

# PUT Payment Terms 

# PUT Due Date

# PUT Bill To 

# PUT 4 Line Items 

# PUT Line Item Information 1

# PUT Line Item Information 2

# PUT Line Item Information 3

# PUT Line Item Information 4

# Click Download Invoice to Directory 

# Send with Google Email Client 
