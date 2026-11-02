from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from credentials import profiles


# ============================================================
# BROWSER
# ============================================================

options = Options()
options.add_argument("--user-data-dir=C:/selenium_profiles/my_scraper")
options.page_load_strategy = "eager"

options.add_argument("--disable-notifications")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")

prefs = {
    "profile.managed_default_content_settings.images": 2
}
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=options)

driver.get("https://instelikes.com/en/app")

input("start----------->")


# ============================================================
# CLICK HELPERS
# ============================================================

def click_xy(x, y):
    driver.execute_cdp_cmd(
        "Input.dispatchMouseEvent",
        {
            "type": "mousePressed",
            "x": x,
            "y": y,
            "button": "left",
            "clickCount": 1
        }
    )

    driver.execute_cdp_cmd(
        "Input.dispatchMouseEvent",
        {
            "type": "mouseReleased",
            "x": x,
            "y": y,
            "button": "left",
            "clickCount": 1
        }
    )


def click_profile():
    click_xy(769, 633)


# ============================================================
# ADD PROFILE BUTTON
# ============================================================

def click_profile_add():
    click_xy(1139, 633)


# ============================================================
# ENTER USERNAME
# ============================================================

def add_user(username):

    # Original field
    click_xy(492, 244)

    # Page shifts after first click
    time.sleep(1)

    # New position
    click_xy(449, 141)

    driver.execute_cdp_cmd(
        "Input.insertText",
        {
            "text": username
        }
    )


# ============================================================
# SUBMIT USERNAME
# ============================================================

def submit_username():
    click_xy(952, 623)


# ============================================================
# CONTINUE / ADD PROFILE
# ============================================================

def continue_veri_btn():
    click_xy(948, 624)


# ============================================================
# PROCESS PROFILES
# ============================================================

try:

    # Open profile menu once
    click_profile()
    time.sleep(1)

    for profile_name, profile_data in profiles.items():

        username = profile_data["login"]

        print(f"\nAdding {profile_name}: {username}")

        # Open add-profile screen
        click_profile_add()
        time.sleep(1)

        # Enter current username
        add_user(username)
        time.sleep(1)

        # Submit
        submit_username()
        time.sleep(5)

        # Continue / add
        continue_veri_btn()
        time.sleep(2)

        print(f"✓ Added: {username}")


    print("\n================================")
    print("ALL PROFILES ADDED")
    print("================================")

    input("Press ENTER to close...")


finally:
    driver.quit()