"""
Hands-On 4 - Selenium Architecture

1. WebDriver
- WebDriver is the core component of Selenium.
- It communicates with the browser using browser drivers like ChromeDriver.
- It executes browser actions such as opening websites, clicking buttons, entering text, etc.

2. Selenium Grid
- Selenium Grid allows tests to run on multiple machines and browsers simultaneously.
- It is mainly used for parallel testing and cross-browser testing.

3. Selenium IDE
- Selenium IDE is a browser extension.
- It records and plays back browser actions.
- It can also generate automation code.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Headless mode
options = Options()
options.add_argument("--headless")

# Launch Chrome
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# Implicit Wait
# Implicit waits are global and may slow down execution.
# Explicit waits are preferred because they wait only when necessary.
driver.implicitly_wait(10)

# Open Website
driver.get("https://www.lambdatest.com/selenium-playground/")

# Print title
print("Page Title:")
print(driver.title)

# Close browser
driver.quit()