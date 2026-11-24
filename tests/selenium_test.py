from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Remote(
    command_executor="http://selenium:4444",
    options=webdriver.ChromeOptions(),
)
try:
    driver.get("http://app-flag-off:5000")
    off_text = driver.find_element(By.ID, "greeting").text
    assert off_text == "Hello from DevOps Lab!", off_text
    print("PASSED: flag OFF shows:", off_text)

    driver.get("http://app-flag-on:5000")
    on_text = driver.find_element(By.ID, "greeting").text
    assert "new feature ON" in on_text, on_text
    print("PASSED: flag ON shows:", on_text)
    driver.save_screenshot("/tests/page.png")
    print("Screenshot saved")
finally:
    driver.quit()
