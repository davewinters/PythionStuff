import time
from selenium import webdriver
from selenium import webdriver.ChromeOptions

driver = webdriver.Chrome()  

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome("/usr/local/bin/chromedriver", chrome_options=options)
driver.get('http://www.google.com/');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()