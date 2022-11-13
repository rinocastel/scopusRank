
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.service import Service

driver = webdriver.Chrome(executable_path="C:/Users/Rino/Documents/Lavoro/Unipd/Scopus/scopus IAS/chromedriver.exe")
url="https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=samsung&btnG="
driver.get(url)
elem = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='gs_r gs_or gs_scl']")))
citatin = elem.text.find("Cite Cited by")
print(citatin)
string_citation=elem.text[citatin+len("Cite Cited by "):].split(" ")[0]
print(string_citation)
#TROVATO!