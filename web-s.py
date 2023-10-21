from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import json

service = Service(executable_path='./chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.infobae.com")

#print(driver.page_source)
news=driver.find_elements(By.CLASS_NAME, "story-card-ctn")



# Python3 code here creating class
class Article:
  def __init__(self, title, href, img):
    self.title = title
    self.href = href
    self.img = img


newsList = []

for index, nw in enumerate(news):
  #print(nw.find_elements(By.TAG_NAME,"a")[0].get_attribute("aria-label"))
  link = nw.find_elements(By.TAG_NAME,"a")[0]
  title = link.get_attribute("aria-label")
  href = link.get_attribute("href")
  img = nw.find_elements(By.TAG_NAME,"img")
  if len(img) > 0:
    img = img[0].get_attribute("src")
  #print(nw.get_attribute("innerHTML"))
  newsList.append(Article(title, href, img))
  #print(newsList[index].title, newsList[index].href, '\n')  
  print(index)  




# Serializing json
json_object = json.dumps([obj.__dict__ for obj in newsList])
# Writing to sample.json
with open("articles.json", "w") as outfile:
  outfile.write(json_object)