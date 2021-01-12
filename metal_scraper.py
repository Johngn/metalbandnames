from selenium.common.exceptions import NoSuchElementException
#from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
import pandas as pd

def get_bands():
    driver = webdriver.Chrome('./chromedriver')
    driver.set_window_size(800, 800)
    url = 'https://www.metal-archives.com/lists/A'
    driver.get(url)
    
    bands = []    

    time.sleep(2)

    for x in range(28):

        while True:
            time.sleep(5)
        
            for i, item in enumerate(driver.find_elements_by_xpath(".//table[@id='bandListAlpha']/tbody[1]//tr")):
                bands.append({
                    "name" : item.find_element_by_xpath(".//td[1]").text,
                    "country" : item.find_element_by_xpath(".//td[2]").text,
                    "genre" : item.find_element_by_xpath(".//td[3]").text,
                    "status" : item.find_element_by_xpath(".//td[4]").text
                    })
                
            try:
                driver.find_element_by_xpath(".//a[@class='next paginate_button paginate_button_disabled']").click()
                break
            except NoSuchElementException:
                driver.find_element_by_xpath(".//a[@id='bandListAlpha_next']").click()

        ul = driver.find_elements_by_xpath(".//ul[@class='menu_style_6']//li")
        ul[x+1].find_element_by_xpath(".//a").click()
        time.sleep(5)
        
    return pd.DataFrame(bands)

df = get_bands()

df.to_csv('./metalbands.csv', index=False)

