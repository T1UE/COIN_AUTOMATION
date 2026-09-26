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

driver.get("https://instelikes.com/en/")
time.sleep(2)

continue_browser_btn = driver.find_element(By.CLASS_NAME, "download-btn.secondary").click()
time.sleep(3)

driver.execute_script("""
document.addEventListener('contextmenu', function(e) {
    e.stopImmediatePropagation();
}, true);
""")
time.sleep(6)
element = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((
        By.XPATH,
        "//*[contains(normalize-space(.), 'Connect')]"
    ))
)
driver.execute_script("arguments[0].click();", element)
time.sleep(5)
