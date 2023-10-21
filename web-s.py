import json
from modules import quitDriver
from modules import parseSite

sitesList = [
  { 
    "id": "infobae",
    "url": "https://www.infobae.com",
    "title": "",
    "css_id": "story-card-ctn", #css keys to find divs etc
    "css_id_fallback": "",
    "elements": [] #filled by modules script
  },
  { 
    "id": "pagina12",
    "url": "https://www.pagina12.com.ar/",
    "title": "",
    "css_id": "headline-card", #css keys to find divs etc
    "css_id_fallback": "article-title",
    "elements": [] #filled by modules script
  },
  { 
    "id": "naka",
    "url": "https://www.nakaoutdoors.com.ar/",
    "title": "",
    "css_id": "product-item", #css keys to find divs etc
    "css_id_fallback": "product-item",
    "elements": [] #filled by modules script
  }
]



#main loop
for index, site in enumerate(sitesList):
  parseSite(site)
quitDriver()


# Serializing json
#json_object = json.dumps([obj.__dict__ for obj in sitesList])
json_object = json.dumps(sitesList, default=lambda __o: __o.__dict__)  
# Writing...
with open("sources.json", "w") as outfile:
  outfile.write(json_object)
