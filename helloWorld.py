import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Safari()
driver.get("http://example.webscraping.com/places/default/search")

def getLinks():
    return driver.find_elements(By.XPATH,"//*[@id=\"results\"]/table/tbody/tr/td/div/a")

driver.find_element(By.XPATH, '//*[@id="search_term"]').send_keys('.')
js = "document.getElementById('page_size').options[1].text = '100';"
driver.execute_script(js)
driver.find_element(By.XPATH, '//*[@id="search"]').send_keys(Keys.ENTER)

wait = WebDriverWait(driver, random.randrange(1, 5))
wait.until(EC.presence_of_all_elements_located((By.XPATH,"//*[@id=\"results\"]/table/tbody/tr/td/div/a")))

links = getLinks()
print(len(links))
countries = [link.text for link in links]
try:
    f = open('input.txt', 'w+')
    for country in countries:
        f.write(country + "\n")
except Exception:
    print("Something didn't go as planned.")
finally:
    f.close()

driver.close()