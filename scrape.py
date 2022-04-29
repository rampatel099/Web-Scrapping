from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException
import time
import pandas as pd


driver = webdriver.Chrome(r"C:\Users\Rohan Nemade\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=24&Tx_State=UP&Tx_District=1&Tx_Market=0&DateFrom=01-Jan-2011&DateTo=31-Mar-2022&Fr_Date=01-Jan-2011&To_Date=31-Mar-2022&Tx_Trend=0&Tx_CommodityHead=Potato&Tx_StateHead=Uttar+Pradesh&Tx_DistrictHead=Agra&Tx_MarketHead=--Select--")

df = pd.DataFrame(columns =["SI_no.", "District_Name", "Market_Name", "Commodity", "Variety", "Grade", "Min_Price_(Rs./Quintal)", "Max_Price_(Rs./Quintal)", "Modal_Price_(Rs./Quintal)", "Price_Date"])
print(df.head())
c = 0

class different_from_previous(object):
    def __init__(self, locator, text_):
        self.locator = locator
        self.text = text_
    def __call__(self, driver):
        try:
            element_text = driver.find_element(*self.locator).text
            return element_text != self.text
        except StaleElementReferenceException:
            return False

while True:
    try:
        WebDriverWait(driver, 10).until(different_from_previous((By.XPATH,'/html/body/form/div[3]/div[6]/div[6]/div[1]/div[2]/div[3]/div/table/tbody/tr[2]/td[1]'),c))
    except TimeoutException:
        pass
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'cphBody_GridPriceData')))
    except TimeoutException:
        pass
    
    c = driver.find_element(By.XPATH,'/html/body/form/div[3]/div[6]/div[6]/div[1]/div[2]/div[3]/div/table/tbody/tr[2]/td[1]').text
    table = driver.find_element_by_id('cphBody_GridPriceData').get_attribute('innerHTML')
    soup = bs(table)
    trs = soup.tbody.find_all('tr')
    
    for tr in trs:
        tds = tr.find_all('td')
        row = [i.text.strip() for i in tds]
        if(len(row) == 10):
            df = df.append(pd.Series(row, index = df.columns), ignore_index=True)
        print(row)
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@src="../images/Next.png"]')))
    except TimeoutException:
        pass

    try:
        l = driver.find_element(By.XPATH, "//input[@src='../images/Next.png']")
        l.click()
    except NoSuchElementException:
        pass
    
df.to_csv("C:/Users/Rohan Nemade/Downloads/Dataset.csv")
