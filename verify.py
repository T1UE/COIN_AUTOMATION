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
#search usernames from the added list
def search_user():
    x, y = 634, 639
    text = "nicollymend413"
    driver.execute_cdp_cmd("Input.dispatchMouseEvent", {
                    "type": "mousePressed", "x": x, "y": y,
                    "button": "left", "clickCount": 1
                })
    driver.execute_cdp_cmd("Input.dispatchMouseEvent", {
            "type": "mouseReleased", "x": x, "y": y,
            "button": "left", "clickCount": 1
        })
    time.sleep(0.1)
    for char in text:
        driver.execute_cdp_cmd("Input.dispatchKeyEvent", {
            "type": "char",
            "text": char,
            "unmodifiedText": char
        })

        driver.execute_cdp_cmd("Input.dispatchKeyEvent", {
            "type": "keyUp",
            "text": char,
            "unmodifiedText": char
})
#selects user
def select_user():
    x, y = 621, 560
    driver.execute_cdp_cmd("Input.dispatchMouseEvent", {
            "type": "mousePressed", "x": x, "y": y,
            "button": "left", "clickCount": 1
        })
    
    driver.execute_cdp_cmd("Input.dispatchMouseEvent", {
        "type": "mouseReleased", "x": x, "y": y,
        "button": "left", "clickCount": 1
    })

# clcik to connect for verification
def click_connect():
    x, y = 597, 316
    driver.execute_cdp_cmd("Input.dispatchMouseEvent", {
            "type": "mousePressed", "x": x, "y": y,
            "button": "left", "clickCount": 1
        })
    
    driver.execute_cdp_cmd("Input.dispatchMouseEvent", {
        "type": "mouseReleased", "x": x, "y": y,
        "button": "left", "clickCount": 1
    })
#confirm verification
def confirm_btn():
    x, y = 952, 628
    driver.execute_cdp_cmd("Input.dispatchMouseEvent", {
                "type": "mousePressed", "x": x, "y": y,
                "button": "left", "clickCount": 1
            })
        
    driver.execute_cdp_cmd("Input.dispatchMouseEvent", {
        "type": "mouseReleased", "x": x, "y": y,
        "button": "left", "clickCount": 1
    })
#types the pass in the field
def enter_pass():
    text = "gnh3yKn3"
    x, y = 447, 400
    driver.execute_cdp_cmd("Input.dispatchMouseEvent", {
            "type": "mousePressed",
            "x": x,
            "y": y,
            "button": "left",
            "clickCount": 1
        })
    driver.execute_cdp_cmd("Input.dispatchMouseEvent", {
        "type": "mouseReleased",
        "x": x,
        "y": y,
        "button": "left",
        "clickCount": 1
    })
    time.sleep(0.1)
    for char in text:
            time.sleep(0.1)
            driver.execute_cdp_cmd("Input.dispatchKeyEvent", {
                "type": "char",
                "text": char,
                "unmodifiedText": char
            })
    
            driver.execute_cdp_cmd("Input.dispatchKeyEvent", {
                "type": "keyUp",
                "text": char,
                "unmodifiedText": char
    })
#agrees the t&c
def agree_t_c():
    x1, y1 = 392, 462
    driver.execute_cdp_cmd("Input.dispatchMouseEvent", {
                    "type": "mousePressed", "x": x1, "y": y1,
                    "button": "left", "clickCount": 1
                })
            
    driver.execute_cdp_cmd("Input.dispatchMouseEvent", {
        "type": "mouseReleased", "x": x1, "y": y1,
        "button": "left", "clickCount": 1
    })
    x2, y2 = 392, 517
    driver.execute_cdp_cmd("Input.dispatchMouseEvent", {
                        "type": "mousePressed", "x": x2, "y": y2,
                        "button": "left", "clickCount": 1
                    })
                
    driver.execute_cdp_cmd("Input.dispatchMouseEvent", {
        "type": "mouseReleased", "x": x2, "y": y2,
        "button": "left", "clickCount": 1
    })

    #  Target: X=964  Y=625 - for continue but not used as resued

def send_tfa_code():
    text = "L6MAJCLNSQKWICBDZYLBRWFNXDW2MHHY"
    x,y=524,465
    driver.execute_cdp_cmd("Input.dispatchMouseEvent", {
                "type": "mousePressed",
                "x": x,
                "y": y,
                "button": "left",
                "clickCount": 1
            })
    driver.execute_cdp_cmd("Input.dispatchMouseEvent", {
        "type": "mouseReleased",
        "x": x,
        "y": y,
        "button": "left",
        "clickCount": 1
    })
    time.sleep(0.1)
    for char in text:
            driver.execute_cdp_cmd("Input.dispatchKeyEvent", {
                "type": "char",
                "text": char,
                "unmodifiedText": char
            })
    
            driver.execute_cdp_cmd("Input.dispatchKeyEvent", {
                "type": "keyUp",
                "text": char,
                "unmodifiedText": char
    })



click_connect()
time.sleep(2)
confirm_btn()
time.sleep(2)
enter_pass()
time.sleep(2)
agree_t_c()
time.sleep(3)
confirm_btn() #used again after pass and t & c clciked
time.sleep(15)
send_tfa_code()
time.sleep(10)
confirm_btn() #used again after tfa given
time.sleep(10)


# click_profile()
# time.sleep(1)
# search_user()
# time.sleep(1)
# select_user()
# time.sleep(1.5)


