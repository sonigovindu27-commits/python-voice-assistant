from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Infow:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)  # keeps window open

        service = Service(r"C:\Program Files\chromedriver-win64\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def get_info(self, query):
        self.query = query
        self.driver.get("https://www.wikipedia.org")


        time.sleep(2)

        # Find the search input box
        search = self.driver.find_element(By.XPATH, '//*[@id="searchInput"]')

        # Type query and press Enter automatically
        search.send_keys(query)
        search.send_keys(Keys.RETURN)


        time.sleep(2)


        try:
            paragraph = self.driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/p[1]').text
            print(f"\n Wikipedia summary for '{query}':\n")
            print(paragraph)
        except Exception as e:
            print(" Could not find information on Wikipedia.")
            print(e)
#assist = Infow()
#assist.get_info("bts")

