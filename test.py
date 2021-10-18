from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd

# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path="./chromedriver.exe"

driver = webdriver.Chrome(driver_path, chrome_options=options)

a=[]
url="https://pnmi.segob.gob.mx/encuesta/exportarExcel/?id_tramite=6770"

for i in range(20000):
    a.append(i)
    itr = url.replace("6770",str(a[i]))
    driver.get(itr)
    print(i)


