import requests
from time import sleep
GSCHOLAR_URL = 'https://scholar.google.com/scholar?&q=samsung&hl=en&as_sdt=0,5'

def get_content_with_selenium(url):
    if 'driver' not in globals():
        global driver
        driver = setup_driver()
    driver.get(url)

    # Get element from page
    el = get_element(driver, "/html/body")
    c = el.get_attribute('innerHTML')

    if any(kw in el.text for kw in ROBOT_KW):
        raw_input("Solve captcha manually and press enter here to continue...")
        el = get_element(driver, "/html/body")
        c = el.get_attribute('innerHTML')


    return c.encode('utf-8')
def setup_driver():
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        from selenium.common.exceptions import StaleElementReferenceException
    except Exception as e:
        print(e)
        print("Please install Selenium and chrome webdriver for manual checking of captchas")

    print('Loading...')
    chrome_options = Options()
    chrome_options.add_argument("disable-infobars")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    return driver

def get_element(driver, xpath, attempts=5, _count=0):
    '''Safe get_element method with multiple attempts'''
    try:
        element = driver.find_element_by_xpath(xpath)
        return element
    except Exception as e:
        if _count<attempts:
            sleep(1)
            get_element(driver, xpath, attempts=attempts, _count=_count+1)
        else:
            print("Element not found")

session = requests.Session()
page=session.get(GSCHOLAR_URL)
c=page.content
if any(kw in c.decode('ISO-8859-1') for kw in ROBOT_KW):
    print("Robot checking detected, handling with selenium (if installed)")
    try:
        c = get_content_with_selenium(url)
    except Exception as e:
        print("No success. The following error was raised:")
        print(e)