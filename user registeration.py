from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By

from time import sleep

import time

driver = webdriver.Chrome()

# Navigate to the tutorilaspoint homepage
driver.get("https://www.tutorialspoint.com/market/business/subscription.jsp?gclid=Cj0KCQiAjbagBhD3ARIsANRrqEs620kaHVg0GCAYXKhZQadzqDOWkjK4bfA0RNscPh02RMhOSnQ3Mp8aAo6sEALw_wcB")

driver.maximize_window()

print("Title of the page: ",driver.title)
# Find the sign-in button and click it
time.sleep(2)

login = driver.find_element(By.XPATH,'//*[@id="navbarCollapse"]/div[2]/div/a')

time.sleep(2)

login.click()

email = driver.find_element(By.XPATH, '//*[@id="user_email"]')

time.sleep(2)

email.send_keys('dhineshambi03@gmail.com')

password = driver.find_element(By.XPATH, '//*[@id="user_password"]')

time.sleep(2)

password.send_keys('DhineshManoj')

time.sleep(2)

login_btn = driver.find_element(By.XPATH, '//*[@id="user_login"]')
login_btn.click()

time.sleep(4)

home = driver.find_element(By.XPATH, '//*[@id="sidedrawer"]/div[1]/a/img')
home.click()
time.sleep(2)

search = driver.find_element(By.XPATH, '//*[@id="search-strings"]')

search.send_keys('python')
time.sleep(2)

search_btn = driver.find_element(By.XPATH, '//*[@id="btnSearch"]/i')
search_btn.click()
time.sleep(2)

product = driver.find_element(By.XPATH, '//*[@id="ebooks_grid"]/div[1]/div[2]/div[2]/div[1]/a')
product.click()

time.sleep(2)

add_wishlist = driver.find_element(By.XPATH, '//*[@id="video-card"]/div/div[4]/a')
add_wishlist.click()

addcart = driver.find_element(By.XPATH,'/html/body/div[4]/div[2]/div[1]/div[2]/div/div[1]/div/div[6]/div[2]/div/div/div/a[1]')
driver.execute_script("arguments[0].click();", addcart)

time.sleep(2)

cartpage = driver.find_element(By.XPATH, '//*[@id="navbarCollapse"]/div[2]/div[1]/a/i')
cartpage.click()

time.sleep(2)

goto_home = driver.find_element(By.XPATH, '/html/body/header/nav/div/a')
goto_home.click()

time.sleep(5)

profile_btn = driver.find_element(By.XPATH, '//*[@id="profileImage"]')
profile_btn.click()

time.sleep(2)

logout = driver.find_element(By.XPATH, '//*[@id="profile-menu"]/li[6]/b/a')

driver.quit()
