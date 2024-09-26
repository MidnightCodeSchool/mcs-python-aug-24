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
url = "https://poojaelectronics.in/product/hollyland-lark-m2-wireless-microphone-india/"
driver.get(url)
xpath = "/html/body/div[1]/div/div/div/main/div[3]/div[2]/p[1]/span[2]"
prince_string = driver.find_element(By.XPATH, xpath).text
price = prince_string.split("₹")[-1].replace(",", "").replace(".", "")
price = float(price)
print(price)