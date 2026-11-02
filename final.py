from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--user-data-dir=C:/selenium_profiles/my_scraper")

driver = webdriver.Chrome(options=options)
driver.get("https://instelikes.com/en/app")

# Track mouse position + capture F8 inside the browser
driver.execute_script("""
window.__mouse = {x: 0, y: 0};
window.__captured = false;

document.addEventListener("mousemove", function(e) {
    window.__mouse.x = e.clientX;
    window.__mouse.y = e.clientY;
});

document.addEventListener("keydown", function(e) {
    if (e.key === "G") {
        window.__captured = true;
    }
});
""")

print("Move your mouse onto the target.")
print("Keep it there and press F8.")

while True:
    captured = driver.execute_script("return window.__captured;")

    if captured:
        pos = driver.execute_script("return window.__mouse;")
        print(f"\nTarget: X={pos['x']}  Y={pos['y']}")
        break

    time.sleep(0.05)

input("Press Enter to close...")