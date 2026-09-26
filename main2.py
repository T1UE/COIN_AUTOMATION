from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
driver = webdriver.Chrome(options=options)

driver.get("https://instelikes.com/en/")

time.sleep(2)
continue_browser_btn = driver.find_element(By.CLASS_NAME, "download-btn.secondary").click()
time.sleep(10)
html = driver.execute_script("return document.documentElement.outerHTML")

with open("login.html", "w", encoding="utf-8") as f:
    f.write(html)

print("HTML saved!")