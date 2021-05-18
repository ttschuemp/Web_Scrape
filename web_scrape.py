# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np
import pyautogui
from selenium import webdriver

class WebScrape: 

    def enter_proxy_auth(self, proxy_username, proxy_password):
        pyautogui.typewrite(proxy_username)
        pyautogui.press('tab')
        pyautogui.typewrite(proxy_password)
        pyautogui.press('enter')
    
    def open_a_page(self, driver, url):
        driver.get(url)
        
    def get_table(self, rows): 
        self.rows = 1+rows
        self.cols = len(driver.find_elements_by_xpath(
            "/html/body/table/tbody/tr/th"))-1
        table = []
        for r in range(2, self.rows +1): # rows+1
            for p in range(1, self.cols+1):
                # obtaining the text from each column of the table
                t = driver.find_element_by_xpath(
                        "/html/body/table/tbody/tr["+str(r)+"]/td["+str(p)+"]").text
                table.append(t)
        table = np.array( table)
        table = np.reshape( table, (self.rows -1, self.cols))
        table[0,0] = table[0,0].split()[-1]
        df= pd.DataFrame(data=table, index=table[:,0], columns = ['Date', '1 col',	
                         '2 col',	'3 col',	'4 col',	'5 col',	'6 col',	
                         '7 col',	'8 col',	'9 col',	'10 col'])
        return df.iloc[: , 1:]

if __name__ == "__main__":

    proxy_username = 'USERNAME'
    proxy_password = 'PASSWORD'
    path = 'C:/.../chromedriver.exe'
    url = 'https://...'
    
    driver = webdriver.Chrome(path)
    
    webscrape = WebScrape()
    webscrape.open_a_page(driver, url)
    webscrape.enter_proxy_auth(proxy_username, proxy_password)
    df = webscrape.get_table(30)
    

        
        
        
        
        
        
        
    