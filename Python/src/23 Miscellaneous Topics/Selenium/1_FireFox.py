import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def doAssert(assertion, message):
    try:
        assert eval(assertion)
    except AssertionError, e:
        print message
        driver.close()
        driver.quit()
        sys.exit()

driver = webdriver.Firefox()
driver.get("http://finance.google.com/finance")
doAssert('"Google Finance:" in driver.title', 'Finance Page error')
    
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("IBM")
elem.send_keys(Keys.RETURN)
doAssert('"International Business Machines" in driver.title', 'wrong title')
doAssert('False', 'test suceeded')




