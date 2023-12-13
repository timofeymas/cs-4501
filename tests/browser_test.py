from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup


def browser_test(tor=False):
    if not tor:
        chrome_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=chrome_service)
        sleep_time = 30
    else:
        # https://stackoverflow.com/questions/15316304/open-tor-browser-with-selenium
        service = Service(ChromeDriverManager().install())
        proxy = "socks5://127.0.0.1:9050"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(f"--proxy-server={proxy}")
        driver = webdriver.Chrome(service=service, options=chrome_options)
        sleep_time = 50

    driver.get("https://coveryourtracks.eff.org/kcarter?aat=1")
    time.sleep(sleep_time)
    element = driver.find_element(By.ID, "summary_sentence")
    text = element.text
    print(text.capitalize())
    driver.get("http://127.0.0.1:8080/")

    text = driver.page_source
    soup = BeautifulSoup(text, 'html.parser')
    text_only = soup.get_text()
    print('USER-DATA:')
    print(text_only.strip())
    driver.quit()
    return