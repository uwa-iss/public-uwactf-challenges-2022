from selenium import webdriver
import time, logging

def view_meme(url: str):
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
    
    for arg in chrome_args:
        chrome_options.add_argument(arg)

    driver = None

    try:
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get(url)
        time.sleep(10)
    except Exception as e:
        logging.error(e)
    finally:
        if not driver is None:
            driver.quit()