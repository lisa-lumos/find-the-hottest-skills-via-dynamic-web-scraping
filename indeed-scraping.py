from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager 
import time

url = 'https://www.indeed.com' 

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) 
driver.get(url) 
wait = WebDriverWait(driver, 10)

# Wait until location search box is loaded
wait.until(EC.visibility_of_element_located((By.ID, "text-input-where")))

keyword = "data"
# search keyword using the location text box
elem_keyword_input = driver.find_element(By.ID,("text-input-what"))
driver.execute_script("arguments[0].focus();", elem_keyword_input)
elem_keyword_input.send_keys(Keys.COMMAND, "a");
elem_keyword_input.send_keys(Keys.DELETE);
elem_keyword_input.send_keys(keyword)
elem_keyword_input.send_keys(Keys.ENTER)
print(f"Keyword entered: {keyword}")
time.sleep(1)

# search location using the location text box
location = "remote"
elem_location_input = driver.find_element(By.ID,("text-input-where"))
# elem_location_input.clear() # this is not working
driver.execute_script("arguments[0].focus();", elem_location_input)
elem_location_input.send_keys(Keys.COMMAND, "a");
elem_location_input.send_keys(Keys.DELETE);
elem_location_input.send_keys(location)
elem_location_input.send_keys(Keys.ENTER)
print(f"Location entered: {location}")
time.sleep(1)

# Only search for jobs posted in the past 24 hrs
btn_date_posted = driver.find_element(By.ID,("filter-dateposted"))
btn_date_posted.click()
time.sleep(1)
list_date_posted = driver.find_element(By.ID,("filter-dateposted-menu"))
list_items = list_date_posted.find_elements(By.TAG_NAME,("li"))
item_1st = list_items[0]
print(f"Date posted selected: {item_1st.text}")
item_1st.click()
time.sleep(1)








time.sleep(5)






















