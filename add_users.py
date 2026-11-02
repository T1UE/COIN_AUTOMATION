from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from credentials import profiles

options = Options()
options.add_argument("--user-data-dir=C:/selenium_profiles/my_scraper")
options.page_load_strategy = 'eager' 

# 2. Disable heavy browser features
options.add_argument("--disable-notifications")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=options)

driver.get("https://instelikes.com/en/app")
input("start----------->")

#clciks to initial homepage profile button
def click_profile():
    x, y = 769, 633
    driver.execute_cdp_cmd("Input.dispatchMouseEvent", {
        "type": "mousePressed", "x": x, "y": y,
        "button": "left", "clickCount": 1
    })

    driver.execute_cdp_cmd("Input.dispatchMouseEvent", {
        "type": "mouseReleased", "x": x, "y": y,
        "button": "left", "clickCount": 1
    })
#clicks to add profile
def click_profile_add():
    x, y = 1139, 633
    driver.execute_cdp_cmd("Input.dispatchMouseEvent", {
            "type": "mousePressed", "x": x, "y": y,
            "button": "left", "clickCount": 1
        })
    
    driver.execute_cdp_cmd("Input.dispatchMouseEvent", {
        "type": "mouseReleased", "x": x, "y": y,
        "button": "left", "clickCount": 1
    })
#gives username
def add_user():
    # Original target
    driver.execute_cdp_cmd("Input.dispatchMouseEvent", {
        "type": "mousePressed",
        "x": 492,
        "y": 244,
        "button": "left",
        "clickCount": 1
    })
    driver.execute_cdp_cmd("Input.dispatchMouseEvent", {
        "type": "mouseReleased",
        "x": 492,
        "y": 244,
        "button": "left",
        "clickCount": 1
    })
    time.sleep(1)
    # New position after the page shifts
    driver.execute_cdp_cmd("Input.dispatchMouseEvent", {
        "type": "mousePressed",
        "x": 449,
        "y": 141,
        "button": "left",
        "clickCount": 1
    })
    driver.execute_cdp_cmd("Input.insertText", {
        "text": "heloisasil729"
    })
    driver.execute_cdp_cmd("Input.dispatchMouseEvent", {
        "type": "mouseReleased",
        "x": 449,
        "y": 141,
        "button": "left",
        "clickCount": 1
    })

#submits the given username
def submit_username():
    x, y = 952, 623
    driver.execute_cdp_cmd("Input.dispatchMouseEvent", {
                "type": "mousePressed", "x": x, "y": y,
                "button": "left", "clickCount": 1
            })
        
    driver.execute_cdp_cmd("Input.dispatchMouseEvent", {
        "type": "mouseReleased", "x": x, "y": y,
        "button": "left", "clickCount": 1
    })

#adds profile
def continue_veri_btn():
    x, y = 948, 624
    driver.execute_cdp_cmd("Input.dispatchMouseEvent", {
                    "type": "mousePressed", "x": x, "y": y,
                    "button": "left", "clickCount": 1
                })
            
    driver.execute_cdp_cmd("Input.dispatchMouseEvent", {
        "type": "mouseReleased", "x": x, "y": y,
        "button": "left", "clickCount": 1
    })

click_profile()
time.sleep(1)
click_profile_add()
time.sleep(1)
add_user()
time.sleep(1)
submit_username()
time.sleep(5)
continue_veri_btn()
time.sleep(2)

driver.quit()