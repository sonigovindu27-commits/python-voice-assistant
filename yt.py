from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class music:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)

        service = Service(r"C:\Program Files\chromedriver-win64\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def play(self, query):

        self.driver.get("https://www.youtube.com/results?search_query=" + query)


        wait = WebDriverWait(self.driver, 15)
        video = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//ytd-video-renderer//a[@id='video-title'])[1]")
        ))
        video.click()

#assist = music()
#assist.play("believer song")
