from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import logging, os, time

import app

def view_uploads():
    """
        This function is just to mimic poly visiting the website
    """
    chrome_args = [
        '--headless',
		'--no-sandbox',
        '--disable-dev-shm-usage',
		'--disable-background-networking',
		'--disable-default-apps',
		'--disable-extensions',
		'--disable-gpu',
		'--disable-sync',
		'--disable-translate',
		'--hide-scrollbars',
		'--metrics-recording-only',
		'--mute-audio',
		'--no-first-run',
		'--safebrowsing-disable-auto-update',
		'--js-flags=--noexpose_wasm,--jitless'
	]

    chrome_options = webdriver.ChromeOptions()

    username = "poly"
    password = os.getenv("POLY_PASSWORD")
    
    for arg in chrome_args:
        chrome_options.add_argument(arg)

    driver = None

    try:
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.implicitly_wait(60)
        driver.get('http://localhost:4243/login.html?noparrots=true')
        username_input = driver.find_element_by_id("username")
        password_input = driver.find_element_by_id("password")
        submit_input = driver.find_element_by_id("submit")

        username_input.send_keys(username)
        password_input.send_keys(password)
        submit_input.click()

        uploads = driver.find_elements_by_tag_name('a')
        links = [upload.get_attribute("href") for upload in uploads]
        for link in links:
            driver.get(link)
            time.sleep(5)

    except Exception as e:
        logging.error(e)
    finally:
        if not driver is None:
            driver.quit()

        # TODO: Wipe the table after viewing it
        # Need a cronjob as well to prevent someone creating a payload that crashes the flask worker and the table never gets clears

def main():
    while True:
        time.sleep(60)
        view_uploads()
        app.clear_uploads()

if __name__ == "__main__":
    main()