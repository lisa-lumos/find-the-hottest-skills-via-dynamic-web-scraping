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

keyword = 'data'
# search keyword using the location text box
elem_keyword_input = wait.until(EC.visibility_of_element_located((By.ID, 'text-input-what')))
driver.execute_script('arguments[0].focus();', elem_keyword_input)
elem_keyword_input.send_keys(Keys.COMMAND, 'a');
elem_keyword_input.send_keys(Keys.DELETE);
elem_keyword_input.send_keys(keyword)
elem_keyword_input.send_keys(Keys.ENTER)
print(f'Keyword entered: {keyword}')

# search location using the location text box
location = 'remote'
elem_location_input = wait.until(EC.visibility_of_element_located((By.ID, 'text-input-where')))
# elem_location_input.clear() # this is not working, due to auto-complete
driver.execute_script('arguments[0].focus();', elem_location_input)
elem_location_input.send_keys(Keys.COMMAND, 'a');
elem_location_input.send_keys(Keys.DELETE);
elem_location_input.send_keys(location)
elem_location_input.send_keys(Keys.ENTER)
print(f'Location entered: {location}')

# Only search for jobs posted in the past 24 hrs
btn_date_posted = wait.until(EC.visibility_of_element_located((By.ID, 'filter-dateposted')))
btn_date_posted.click()
list_date_posted = driver.find_element(By.ID,('filter-dateposted-menu'))
list_items = list_date_posted.find_elements(By.TAG_NAME,('li'))
item_1st = list_items[0]
print(f'Date posted selected: {item_1st.text}')
item_1st.click()

# get num of postings
div_job_count = driver.find_element(By.CLASS_NAME,('jobsearch-JobCountAndSortPane-jobCount'))
print(f'Count of jobs: {div_job_count.text}')

div_job_cards = driver.find_element(By.ID,('mosaic-provider-jobcards'))
ul_job_cards = div_job_cards.find_element(By.TAG_NAME,('ul'))
li_job_cards = ul_job_cards.find_elements(By.XPATH, ('./li'))


scraped_jobs_count = 0
single_page_job_idx = 0
global_job_idx = 0
page_number = 0
for li_job_card in li_job_cards:
    print(f'\n-------------- page {page_number+1}, local listing #{single_page_job_idx+1}, global listing #{global_job_idx+1}')
    # print(li_job_card.get_attribute('innerHTML') + '\n')
    try: 
        anchor_job_title = li_job_card.find_element(By.XPATH, ('.//*//a'))
        anchor_job_title.click()
        wait.until(EC.visibility_of_element_located((By.ID, 'jobsearch-ViewjobPaneWrapper')))

        div_details_pane = driver.find_element(By.ID,('jobsearch-ViewjobPaneWrapper'))
        span_job_title = div_details_pane.find_element(By.XPATH, ('.//*//span'))
        # print(f'Job title: {h2_header.text}')
        print(driver.execute_script("return arguments[0].firstChild.textContent;", span_job_title).strip())
        # print(li_job_card.text)
        scraped_jobs_count += 1
        single_page_job_idx += 1
        global_job_idx += 1
        # if (scraped_jobs_count == 3): break
    except:
        print("skipped an invalid job card")

time.sleep(10)






















