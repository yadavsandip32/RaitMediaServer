from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Firefox()

driver.get("https://www.google.com/search?q=site%3Ahttps%3A%2F%2Ftimesofindia.com+inurl%3Ahiv&rlz=1C1CHBF_enIN801IN801&source=lnt&tbs=cdr%3A1%2Ccd_min%3A1%2F1%2F2010%2Ccd_max%3A&tbm=")

section = driver.find_element_by_id('rso')

elems = driver.find_elements_by_xpath("//*[@class='g']/div/div/div/a[@href]")
iter = 0
for elem in elems:
    print(elem.get_attribute("href")) 
    iter = iter + 1
    if iter == 10:
        break

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)


next_page = driver.find_elements_by_xpath("//*[@id='nav']/tbody/tr/td/a[1]")
for page in next_page:
    page.click()