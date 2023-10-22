from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#import shortuuid
#from WebElement import WebElement
#import copy
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

service = Service(executable_path='./chromedriver.exe')
options = webdriver.ChromeOptions()
#options.add_argument("--headless=new") # for Chrome >= 109
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2 }) 
driver = webdriver.Chrome(service=service, options=options)


driver.get('https://www.instagram.com/')
driver.maximize_window()
#WebDriverWait(driver, 10)
time.sleep(5)
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

username.send_keys("")
password.send_keys("")
submit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()


time.sleep(5)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Not Now']"))).click()



#scroll down 2 times
#increase the range to sroll more
images = driver.find_elements(By.TAG_NAME, 'img')
y = 1000
for timer in range(0,20):
    driver.execute_script("window.scrollTo(0, "+str(y)+")")
    y += 1000  
    time.sleep(1)


time.sleep(1)
images = driver.find_elements(By.TAG_NAME, 'img')
time.sleep(2)
print(images)
#images.pop(0) #remove weird data
imgList = []

for index, image in enumerate(images): # 1 removes first item, weird data,starts index 0
    #if(index>0):
    imgList.append(image.get_attribute("src"))
    #image.screenshot('Download-Location' + ' (' + str(index) + ').png')
#imgList.pop(0)


prefixes = ('data:image/', 'bye')
#list = ['hi', 'helloyou', 'holla', 'byeyou', 'hellooooo']
for word in imgList[:]:
    if word.startswith(prefixes):
        imgList.remove(word)

print(imgList)
# Serializing json
json_object = json.dumps(imgList)  #investigate json serializing
# Writing...
with open("sources.json", "w") as outfile:
  outfile.write(json_object)



import os
import wget

path = os.getcwd()
path = os.path.join(path, "pics")

#create the directory
os.mkdir(path)


#download images
#download images
counter = 0
for index, image in enumerate(imgList):
    save_as = os.path.join(path, "pic" + str(index) + '.jpg')
    wget.download(image, save_as)
    counter += 1
'''

import os
import wget

path = os.getcwd()
path = os.path.join(path, "www" + "s")

#create the directory
os.mkdir(path)

path

#download images
#download images
counter = 0
for index, image in enumerate(imgList):
    save_as = os.path.join(path, "2222" + str(index) + '.jpg')
    wget.download(image, save_as)
    counter += 1

'''

'''
print(imgList)
# Serializing json
json_object = json.dumps(imgList, default=lambda __o: __o.__dict__)  #investigate json serializing
# Writing...
with open("sources.json", "w") as outfile:
  outfile.write(json_object)




'''