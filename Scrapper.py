import time
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from requests.packages.urllib3.exceptions import InsecureRequestWarning

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Suppress only the single InsecureRequestWarning from urllib3
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


# WHAT WE WANT TO RETRIEVE 
# # GSTIN No, PAN No, Name, Permanent Address 


# Set up the Selenium WebDriver

path = "C:\msedgedriver.exe"
service = Service(path)  
driver = webdriver.Edge(service=service)


# Open the target website
driver.get('https://hprera.nic.in/PublicDashboard')

# Creating lists
LINKS = []
PROJECT_NAMES = []
details = []

try:
    registered_projects = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="tab_project_main-filtered-data"]/ul/li[1]/a'))
    )
    
    for i in range(7):
        target = driver.find_elements(By.XPATH, '//*[@id="reg-Projects"]/div/div/div['+ str(i) +']')
        
        for t in target:
            # print(t.text)
            links = t.find_elements(By.TAG_NAME, 'a')
            project_names = t.find_elements(By.TAG_NAME, 'span')
            proj_names = [item.text for item in project_names if item.text.isupper()]
            PROJECT_NAMES.append(proj_names) #[['KAISVILLE COUNTRY HOMES'], ['SOMA NEW TOWNS'], ['MB BUILDERS'], ['AMOHA RESIDENCES'], ['AMILA HILLS'], ['AMRAVATI HILLS, MOUZA LAVIKHURD, DISTT. SOLAN']] project list
            
            link_names = [item.text for item in links if item.text.isupper()]
            LINKS.append(link_names) #[['RERAHPKUP01180019'], ['RERAHPSOP10170012'], ['HPRERAUNA2022007/P'], ['RERAHPKAP11170013'], ['RERAHPSHP11170015'], ['RERAHPSOP12170016']] links list
            
    for link in LINKS:
        a = driver.find_element(By.LINK_TEXT, link[0])
        a.click()
        time.sleep(5)
        
        clicked_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, link[0]))
        )
        
        whole_table = driver.find_element(By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody')
        
        all_tr_tags = whole_table.find_elements(By.TAG_NAME, 'tr')
        
        for td in all_tr_tags:
            all_td_tags = td.find_elements(By.TAG_NAME, 'td')
        
            for i, tag in enumerate(all_td_tags):
                if tag.text == "Name":
                    # Check if there is a next td element
                    if i + 1 < len(all_td_tags):
                        next_td = all_td_tags[i + 1]
                        name = next_td.text
                        print(f"Name: {name}")
                        
                if tag.text == "GSTIN No.":
                    # Check if there is a next td element
                    if i + 1 < len(all_td_tags):
                        next_td = all_td_tags[i + 1]
                        GST_NO = next_td.text
                        print(f"GST NO: {GST_NO}")
                        
                if tag.text == "PAN No.":
                    # Check if there is a next td element
                    if i + 1 < len(all_td_tags):
                        next_td = all_td_tags[i + 1]
                        PAN_NO = next_td.text
                        print(f"PAN No.: {PAN_NO}")
                        
                if tag.text == "Permanent Address":
                    # Check if there is a next td element
                    if i + 1 < len(all_td_tags):
                        next_td = all_td_tags[i + 1]
                        permenant_address = next_td.text
                        print(f"permenant_address: {permenant_address}")
                        
        # name = driver.find_element(By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr[1]/td[2]').text
        # GST_NO = driver.find_element(By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr[8]/td[2]/span').text
        # PAN_NO = driver.find_element(By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr[7]/td[2]/span').text
        # permenant_address = driver.find_element(By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr[14]/td[2]/span').text
        
        close_button = driver.find_element(By.XPATH, '//*[@id="modal-data-display-tab_project_main"]/div/div/div[1]/button')
        close_button.click()
        
                    
        details.append({
            'Rera No': link[0],
            'Name': name,
            'GSTIN No': GST_NO,
            'PAN No': PAN_NO,
            'Permanent Address': permenant_address
        })

    time.sleep(5)

finally:
    df = pd.DataFrame(details)
    print(df)
    df.to_csv('C:/Users/shrut/OneDrive/Desktop/Scrape_Assignment/scraped_data.csv', index=False)
    print("File Saved !!!")
    driver.quit()