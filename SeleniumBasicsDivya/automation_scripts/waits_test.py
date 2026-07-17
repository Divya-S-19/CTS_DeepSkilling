import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://www.lambdatest.com/selenium-playground/bootstrap-alert-messages-demo")

# ----------------------------------
# Step 36
# ----------------------------------

button = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.ID,"autoclosable-btn-success"))
)

button.click()

alert = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR,".alert-success"))
)

assert "successfully" in alert.text.lower()

print("Explicit Wait Passed")

# ----------------------------------
# Step 37
# ----------------------------------

start = time.time()

driver.refresh()

driver.find_element(By.ID,"autoclosable-btn-success").click()

time.sleep(3)

print("time.sleep :", round(time.time()-start,2),"seconds")

driver.refresh()

start = time.time()

driver.find_element(By.ID,"autoclosable-btn-success").click()

WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR,".alert-success"))
)

print("Explicit Wait :", round(time.time()-start,2),"seconds")

# Explicit waits are faster because
# they continue immediately once the
# condition becomes true.

# ----------------------------------
# Step 38
# ----------------------------------

driver.refresh()

button = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.ID,"autoclosable-btn-success"))
)

button.click()

"""
visibility_of_element_located:
Element is present and visible.

element_to_be_clickable:
Element is visible, enabled and ready for clicking.
"""

# ----------------------------------
# Step 39
# ----------------------------------

driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")

wait = WebDriverWait(
    driver,
    timeout=10,
    poll_frequency=0.5,
    ignored_exceptions=[NoSuchElementException]
)

table = wait.until(
    EC.visibility_of_element_located((By.ID,"example"))
)

print("Table Loaded Successfully")

driver.quit()