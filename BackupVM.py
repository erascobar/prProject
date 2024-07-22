from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Edge()
driver.get("X")
driver.maximize_window()
driver.implicitly_wait(7)

options = webdriver.EdgeOptions()
options.add_argument('--ignore-certificate-errors')


# Log in screen
driver.find_element(By.ID,"username").send_keys('USER')
driver.find_element(By.ID,"password").send_keys('PASS')
wait = WebDriverWait(driver, 8)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div[normalize-space(text())='Sign In']")))
driver.find_element(By.XPATH,"//XX-button/button[@id='sign-in-button']").click()

# Navigation to VM and search for VM
driver.find_element(By.XPATH,"//div/span[normalize-space(text())='Virtual Machines']").click()
time.sleep(7)

# Search for VM
searchbox = driver.find_element(By.CSS_SELECTOR,"input[type='search']")
searchbox.send_keys("VM")
time.sleep(3)
# Click on VM
driver.find_element(By.XPATH,"(//div/span[normalize-space(text())='VM'])[1]").click()
time.sleep(5)

# Starting a backup
driver.find_element(By.XPATH,"(//button[@type='button'])[2]").click()
#driver.find_element(By.XPATH,"//div/input[@id='common.toolbar.backup.forceFullBackup.label']").click()
driver.find_element(By.XPATH,"//button[@id='yes-btn']").click()

# driver.find_element()

time.sleep(500)

