import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def extract_data(link):
    try:
        if not link.startswith("http"):
            link = "https://" + link

        opt = Options()
        opt.add_argument("--headless")

        driver = webdriver.Chrome(options=opt)
        driver.get(link)

        time.sleep(3)

        print(driver.title)

        body = driver.find_element(By.TAG_NAME, "body")
        print(body.text)

        all_links = driver.find_elements(By.TAG_NAME, "a")
        for l in all_links:
            href = l.get_attribute("href")
            if href != None:
                print(href)

        driver.quit()

    except Exception as e:
        print("Error:", e)


if len(sys.argv) != 2:
    print("Usage: python scraper.py <website>")
else:
    extract_data(sys.argv[1])
