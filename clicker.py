from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from time import sleep
#import os, wget

########################################################################
# Set ChromeDriverPath or use the Script ChromeDriver.py    
# it will download the compatible chromedriver to your user home repo  
# Set FB User & Pass    
########################################################################



fbuser = "" 
fbpass = ""
service = Service(executable_path='./chromedriver.exe')
site =  'https://mercadolibre.com.ar'

class browser:
    def __init__(self, driver,DEFAULT_TIMEOUT,delay):
        self.timeout = DEFAULT_TIMEOUT
        self.delay = delay
        self.driver = driver
        #self.chrome_options = webdriver.ChromeOptions()

    def enable_download_headless(self,download_dir):
        self.driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
        params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
        self.driver.execute("send_command", params)

    def elementXPATH(self,xpath):
        self.Welement = WebDriverWait(self.driver,self.delay).until(EC.presence_of_element_located((By.XPATH, xpath)))

    def elementTEXT(self, text):
        self.Welement = self.driver.find_element(By.LINK_TEXT, text)

    def elementsCLASS(self, key):
        self.Welement = self.driver.find_elements(By.CLASS_NAME, key)#como buscarlo solo?

    def click(self, index = False):
            if (index == 0 and type(index) == int or index and type(index) == int ):
                self.Welement[index].click()     
            else:
                self.Welement.click()
            sleep(1)

    def send(self,text):
            self.Welement.send_keys(text)

    def get(self,site):
        self.driver.get(site)
        sleep(4)

    def Execute(self,scripts):
        self.driver.execute_script(scripts,self.Welement)

    def text(self):
        return self.Welement.text

    def attribute(self,att):
        return self.Welement.get_attribute(att)


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('log-level=2')
chrome_options.add_argument('--disable-notifications')
chrome_options.add_argument('--disable-popup-blocking')
driver = webdriver.Chrome(options=chrome_options,service=service)
bot = browser(driver=driver,DEFAULT_TIMEOUT=20,delay=10)





bot.driver.maximize_window()
bot.get(site)
#bot.elementXPATH('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
bot.elementTEXT('Categorías')
bot.click()
categories = bot.elementsCLASS('nav-categs-departments__list')
for idx, x in enumerate(bot.Welement):
    print(idx, x)
    bot.click(idx)
    bot.elementTEXT('Categorías')
    bot.click()
    bot.elementsCLASS('nav-categs-departments__list')
#bot.elementsCLASS('nav-categs-departments__list')
#bot.click(0)
#bot.elementTEXT('Categorías')
#bot.click()
#bot.elementsCLASS('nav-categs-departments__list')
#bot.click(1)
#bot.click(bot.Welement_index)
#bot.element('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
#bot.click()


#homepage = bot.driver.window_handles[0]
#fbPopUp = bot.driver.window_handles[1]

#bot.driver.switch_to.window(fbPopUp)

#bot.element('//*[@id="email"]')
#bot.send(fbuser)
#bot.element('//*[@id="pass"]')
#bot.send(fbpass)

#bot.element('//*[@id="u_0_0"]')
#bot.click()

#bot.driver.switch_to.window(homepage)

#bot.element('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
#bot.click()






