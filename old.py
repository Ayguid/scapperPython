from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='./chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.infobae.com")

#print(driver.page_source)

h2s=driver.find_elements(By.CSS_SELECTOR,"h2")


# Python3 code here creating class
class article:
  def __init__(self, title, text):
    self.title = title
    self.text = text

news = []
for obj in h2s:
  #print(obj.text)
  news.append(article(obj.text, ''))  

print(news[0])