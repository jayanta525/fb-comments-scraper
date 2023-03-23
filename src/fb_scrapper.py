#!/usr/local/bin/python3
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

import fb_helper
import process_bs

def set_chrome_options() -> None:
    """Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    return chrome_options

def main(email, password, urls, out_dir):
    chrome_opts = set_chrome_options()
    driver = webdriver.Chrome(options=chrome_opts)
    fb_helper._login(driver, email, password)

    # loop until lines array is over
    for url in urls:
        print("Scraping URL: " + url)
        driver.get(url)
        time.sleep(2)
        fb_helper._get_comments(driver)
        # get the page source
        bs_data = driver.page_source
        # pass bs_data to func
        process_bs.main(bs_data, out_dir)
        print("Done")
    driver.close()

if __name__ == '__main__':
    # _process_bs()
    print("This module cannot be run directly. Please run main.py instead.")