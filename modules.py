from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import uuid
from WebElement import WebElement

service = Service(executable_path='./chromedriver.exe')
options = webdriver.ChromeOptions()
#options.add_argument("--headless=new") # for Chrome >= 109
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=service, options=options)


def getSiteTitle():
    return driver.title

def getElementImgs(element):
    imgs = element.find_elements(By.TAG_NAME,"img")
    retList = []
    if len(imgs) > 0:
        for index, img in enumerate(imgs):
            retList.append(img.get_attribute("src"))
    return retList

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


def parseSite(site):
    #pagina 12
    driver.get(site['url'])
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    site['title'] = getSiteTitle()  
    elements = driver.find_elements(By.CLASS_NAME, site['css_id'])
    parsedList = []
    for index, element in enumerate(elements):
        randomId =  str(uuid.uuid4())
        title = getElementTitle(element) #redo rethink
        links = getElementLinksData(element)
        imgs = getElementImgs(element)
        parsedList.append(WebElement(randomId, title, links, imgs))
    site['elements'] = parsedList

def quitDriver():
    driver.quit()