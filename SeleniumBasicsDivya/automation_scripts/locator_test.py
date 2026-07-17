from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")

# -------------------------------
# Step 32 - All Locator Strategies
# -------------------------------

# By.ID
driver.find_element(By.ID, "user-message")

# By.NAME
driver.find_element(By.NAME, "user-message")

# By.CLASS_NAME
driver.find_element(By.CLASS_NAME, "form-control")

# By.TAG_NAME
driver.find_element(By.TAG_NAME, "input")

# By.XPATH (Relative)
driver.find_element(By.XPATH, "//input[@id='user-message']")

# By.XPATH (Absolute)
# NOTE:
# Copy the absolute XPath using F12 -> Copy -> Copy Full XPath.
# Example (may change if website updates):
# driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/input")

print("All locator strategies executed successfully.")

# -------------------------------
# Step 33 - CSS Selectors
# -------------------------------

# By ID
driver.find_element(By.CSS_SELECTOR, "#user-message")

# By Attribute
driver.find_element(By.CSS_SELECTOR, "input[name='user-message']")

# Parent > Child
driver.find_element(By.CSS_SELECTOR, "div > input")

print("CSS Selectors executed successfully.")

# -------------------------------
# Step 34 - Checkbox Demo
# -------------------------------

driver.get("https://www.lambdatest.com/selenium-playground/checkbox-demo")

label = driver.find_element(By.XPATH, "//label[text()='Option 1']")
print("Label:", label.text)

labels = driver.find_elements(By.XPATH, "//label[contains(text(),'Option')]")

print("Labels found:", len(labels))

for item in labels:
    print(item.text)

# -------------------------------
# Step 35 - Locator Ranking
# -------------------------------

"""
Preferred Locator Order

1. ID
2. NAME
3. CSS Selector
4. XPath (Relative)
5. CLASS_NAME
6. TAG_NAME
7. XPath (Absolute)

Reason:
- ID is unique and fastest.
- NAME is usually unique.
- CSS is fast and readable.
- Relative XPath is flexible.
- CLASS_NAME may not be unique.
- TAG_NAME returns many elements.
- Absolute XPath easily breaks if page structure changes.
"""

driver.quit()