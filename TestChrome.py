from selenium import webdriver
from selenium.webdriver.chrome.options import Options
user = ""
pwd = ""
#driver = webdriver.Chrome()

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")


driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("http://www.facebook.com")
assert "Facebook" in driver.title
#elem = driver.find_element_by_id("email")
#elem.send_keys(user)
#elem = driver.find_element_by_id("pass")
#elem.send_keys(pwd)
#elem.send_keys(Keys.RETURN)

driver.close()
