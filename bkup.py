#modules old
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from Article import Article
import uuid
service = Service(executable_path='./chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument("--headless=new") # for Chrome >= 109
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=service, options=options)



def findText(link):
    elementText = link.text # sometimes doesnt work
    if not elementText:
        elementText = link.get_attribute("innerText")
    if not elementText:
        elementText = link.get_attribute("textContent")
    if not elementText:
        elementText = link.get_attribute("textContent")
    # print("elementText=%s" % elementText)
    return elementText
    


def findFallbackText(element, key):
    return element.find_elements(By.CLASS_NAME, key)[0].find_elements(By.TAG_NAME,"a")[0].get_attribute("innerText")    
    


def parseSite(site):
    #pagina 12
    driver.get(site['url']) 
    news=driver.find_elements(By.CLASS_NAME, site['data_id'])
    returnList = []
    for index, nw in enumerate(news):
        link = nw.find_elements(By.TAG_NAME,"a")[0]
        title = findText(link) if findText(link) else findFallbackText(nw, site['data_id_fallback'])
        href = link.get_attribute("href")
        img = nw.find_elements(By.TAG_NAME,"img")
        if len(img) > 0:
            img = img[0].get_attribute("src")
        randomId =  str(uuid.uuid4())
        returnList.append(Article(randomId, title, href, img))
        #next(x for x in listtoAppend if x["name"] == 'infobae' )['news'].append(Article(title, href, img))
        print(index, title)
    return returnList 

def quitDriver():
    driver.quit()