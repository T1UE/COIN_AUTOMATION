from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--user-data-dir=C:/selenium_profiles/my_scraper")
driver = webdriver.Chrome(options=options)

driver.get("https://instelikes.com/en/app")
input("")

# home_page_canvas = driver.find_element(By.TAG_NAME, "canvas")

# print(home_page_canvas.size)

from selenium.webdriver.common.by import By

result = driver.execute_script("""
return [...document.querySelectorAll('*')].filter(el => {
    return el.outerHTML && el.outerHTML.includes('/pictures/7662424577461145806');
}).map(el => el.outerHTML);
""")

print(result)