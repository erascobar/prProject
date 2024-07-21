from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Edge()
driver.get("BC")
# BC instead of the real adress for security policy
driver.maximize_window()
driver.implicitly_wait(7)

options = webdriver.EdgeOptions()
options.add_argument('--ignore-certificate-errors')


# Log in screen
driver.find_element(By.ID,"username").send_keys('admin')
driver.find_element(By.ID,"password").send_keys('admin')
wait = WebDriverWait(driver, 8)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div[normalize-space(text())='Sign In']")))
driver.find_element(By.XPATH,"//XX-button/button[@id='sign-in-button']").click()

# Navigation to Targets
driver.find_element(By.XPATH,"//div/span[normalize-space(text())='Targets']").click()
time.sleep(4)

# First Target
# Target SMB
addTarget = driver.find_element(By.XPATH,"(//button[@type='button'])[1]")
addTarget.click()
driver.find_element(By.XPATH,"//div/button[@id='target.type.label.smb']").click()
driver.find_element(By.ID,"next-btn-add-edit-general").click()

# First box
name = driver.find_element(By.ID,"name")
name.send_keys("Original SMB")
driver.find_element(By.ID,"next-btn-add-edit-general").click()

# Second box
domain = driver.find_element(By.ID,"domain")
domain.send_keys("X")
username = driver.find_element(By.ID,"username")
username.send_keys("X")
password = driver.find_element(By.ID,"password")
password.send_keys("X")
address = driver.find_element(By.ID,"address")
address.send_keys("X")
sharedPath = driver.find_element(By.ID,"sharedPath")
sharedPath.send_keys("X")
driver.find_element(By.ID,"save-btn-add-edit-specific").click()

time.sleep(10)

# Second Target
# Target Archive SMB
addTarget = driver.find_element(By.XPATH,"(//button[@type='button'])[1]")
addTarget.click()
driver.find_element(By.XPATH,"//div/button[@id='target.type.label.smb']").click()
driver.find_element(By.ID,"next-btn-add-edit-general").click()

# First box
name = driver.find_element(By.ID,"name")
name.send_keys("Archive SMB")
# Archive turned on
driver.find_element(By.CLASS_NAME,"switch-button").click()

driver.find_element(By.ID,"next-btn-add-edit-general").click()

# Second box
domain = driver.find_element(By.ID,"domain")
domain.send_keys("X")
username = driver.find_element(By.ID,"username")
username.send_keys("X")
password = driver.find_element(By.ID,"password")
password.send_keys("X")
address = driver.find_element(By.ID,"address")
address.send_keys("X")
sharedPath = driver.find_element(By.ID,"sharedPath")
sharedPath.send_keys("X")
driver.find_element(By.ID,"save-btn-add-edit-specific").click()

time.sleep(10)


# Fourth Target
# Target Original AWS
addTarget = driver.find_element(By.XPATH,"(//button[@type='button'])[1]")
addTarget.click()
driver.find_element(By.XPATH,"//div/button[@id='target.type.label.amazon']").click()
driver.find_element(By.ID,"next-btn-add-edit-general").click()

# First box
name = driver.find_element(By.ID,"name")
name.send_keys("Original AWS")
# Archive turned on
# driver.find_element(By.CLASS_NAME,"switch-button").click()
driver.find_element(By.ID,"next-btn-add-edit-general").click()
time.sleep(4)
# Second box
endpoint = driver.find_element(By.ID,"serviceEndPoint")
endpoint.send_keys("X")
bucket = driver.find_element(By.ID,"bucketName")
bucket.send_keys("X")
access = driver.find_element(By.ID,"accessKeyId")
access.send_keys("X")
secret = driver.find_element(By.ID,"secretAccessKey")
secret.send_keys("X")
driver.find_element(By.ID,"save-btn-add-edit-specific").click()

time.sleep(500)

