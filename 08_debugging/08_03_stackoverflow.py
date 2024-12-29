"""
Go to https://stackoverflow.com/questions/tagged/python?tab=Newest
and look through some of the newest questions tagged with "Python".

Pick one of the questions that includes a code snippet and try to get
it working in your local environment.

Use your debugger to attempt to solve the challenge that the user ran into.
If you can solve it, post your solution as an answer to the question.
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = "https://www.wsj.com/market-data/stocks/us"
driver.get(url)

time.sleep(10)

try:
    element = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[1]/div[2]/div/div[2]/table/tbody[1]/tr/td[2]")
    data = element.text
    print(f"Found data: {data}")
except Exception as e:
    print(f"Error: {e}")

driver.quit()