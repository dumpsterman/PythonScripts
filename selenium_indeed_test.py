from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def clearElement(element):
    CTRL = u'\ue009'
    DELETE = u'\ue017'

    actions = webdriver.ActionChains(driver)
    actions.click(element)
    actions.key_down(CTRL).key_down('a').perform()
    actions.key_up(CTRL).key_up('a').send_keys(DELETE).perform()


driver = webdriver.Firefox()

driver.get('https://www.indeed.com/')

what = input('What job title are you looking for? ')
where = input('Where are you looking? City, State or Zip: ')

try:
    elementWhat = driver.find_element_by_id("text-input-what")
    elementWhere = driver.find_element_by_id("text-input-where")
    print("text-input")
except:
    elementWhat = driver.find_element_by_id("what")
    elementWhere = driver.find_element_by_id("where")
    print("no text-input")

clearElement(elementWhere)

elementWhat.send_keys(what)
elementWhere.send_keys(where)
elementWhere.submit()

WebDriverWait(driver, 10).until(EC.url_contains('jobs?q'))

allTitles = driver.find_elements_by_xpath("//a[@title]")
if(allTitles == []):
    print('error')
for i in allTitles:
    print(i.text)
