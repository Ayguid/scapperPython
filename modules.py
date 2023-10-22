from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import shortuuid
from WebElement import WebElement
import copy
import time

service = Service(executable_path='./chromedriver.exe')
options = webdriver.ChromeOptions()
#options.add_argument("--headless=new") # for Chrome >= 109
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2 }) 
driver = webdriver.Chrome(service=service, options=options)


def getSiteTitle():
    return driver.title

def getElementImgs(element):
    imgs = element.find_elements(By.TAG_NAME,"img")
    retList = []
    if len(imgs) > 0:
        for index, img in enumerate(imgs):
            retList.append(img.get_attribute("src"))
    return list(set(retList))#set is to remove duplicates

def getElementLinksData(element): #one for now
    links= element.find_elements(By.TAG_NAME,"a")
    retList = []
    if len(links) > 0:
        for index, link in enumerate(links):
            retList.append(link.get_attribute("href"))
    return list(set(retList))#set is to remove duplicates

def getElementTitle(element): #one for now
    elementText = element.text # sometimes doesnt work
    if not elementText:
        elementText = element.get_attribute("innerText")
    if not elementText:
        elementText = element.get_attribute("textContent")
    if not elementText:
        elementText = element.get_attribute("textContent")
    # print("elementText=%s" % elementText)
    return elementText

def __scroll_down_page(speed=8):
    current_scroll_position, new_height= 0, 1
    while current_scroll_position <= new_height:
        current_scroll_position += speed
        driver.execute_script("window.scrollTo(0, {});".format(current_scroll_position))
        new_height = driver.execute_script("return document.body.scrollHeight")

def parseSite(site):
    #copy element, so as to not alter original element
    parsedSite = copy.copy(site)
    driver.get(site['url'])
    time.sleep(3) # take a pause 3 seconds ,,,implicitly_wait(5) hangs script... 
    __scroll_down_page()
    time.sleep(2)
    #driver.implicitly_wait(5) # seconds
    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    parsedSite['title'] = getSiteTitle() 
    elements = driver.find_elements(By.CLASS_NAME, parsedSite['css_id'])
    parsedElements = []
    for index, element in enumerate(elements):
        randomId =  parsedSite['id'] + "-" + shortuuid.uuid()
        title = getElementTitle(element) #redo rethink
        links = getElementLinksData(element)
        imgs = getElementImgs(element)
        html = element.get_attribute('outerHTML')
        webElement = WebElement(randomId, title, links, imgs, html) 
        parsedElements.append(webElement)
    parsedSite['elements'] = parsedElements
    return parsedSite

def quitDriver():
    driver.quit()