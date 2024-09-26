"""
poetry add selenium
poetry add chromedriver-autoinstaller
"""

from time import sleep
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By


chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

driver = webdriver.Chrome()
url = "https://google.com"
driver.get(url)
search_box = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
search_box.send_keys("หมีเนย ราคา")
search_box.submit()