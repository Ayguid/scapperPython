import json

class WebElement:
  def __init__(self, id, title, links, imgs, html):
    self.id = id
    self.title = title
    self.links = links
    self.imgs = imgs,
    self.html = html

  def toJSON(self):
    return json.dumps(self, default=lambda o: o.__dict__)  #investigate json serializing