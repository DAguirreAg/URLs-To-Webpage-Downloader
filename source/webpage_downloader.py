import time
import datetime
from typing import List, Dict
import selenium
from selenium import webdriver
from config import Config
import utils

def download_webpage(driver: selenium.webdriver.remote.webdriver.WebDriver, url: str, waittime: float, save_to_path: str):

    # Go to url
    driver.get(url)
    
    # Wait to load page
    time.sleep(waittime)
    
    # Get HTML content
    html = driver.page_source
    
    # Get filename
    filename = utils.get_filename()
    
    # Save html with metadata
    utils.save_webpage(url, html, save_to_path, filename)


def download_webpages(Config: Config, urls: List[Dict[str, str]]):

    try:
        # Get driver
        driver = webdriver.Remote(Config.SELENIUM_URL, options=webdriver.ChromeOptions())
    
        # Download each URL
        amount_items = len(urls)
        errors = []
        for i, item in enumerate(urls):
    
            # Extract parameters
            url = item['url']
            save_to_path = item['save_to_path']
            
            print(f'Progress: {i+1}/{amount_items}. URL: {url}')    
    
            # Download and save a webpage
            try:
                download_webpage(driver, url, Config.WAIT_PAUSE_TIME, save_to_path)

            except Exception as e:
                errors.append(f'url: {url}. Error: {e}')
            
    except:
        raise
        
    finally:
        driver.quit()

    print(len(errors))
    if errors:
        raise Exception(f'ERRORs found: {errors}')

def main(frequency):

    # Load URLS list
    url_list = utils.load_json(Config.URL_LIST)

    # Get urls to download
    urls = url_list[frequency]

    # Download webpages
    download_webpages(Config, urls)

if __name__=='__main__':

    # Loop over all the frequencies
    for frequency in Config.FREQUENCIES:
        print(f'Downloading: {frequency} related items.')
        main(frequency)

