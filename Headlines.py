#   Scraper and aggregator, will scrape top headlines for a series of websites from top contributors 
#   Top contributors will be sourced from a variety of viewpoints
#   Ex. Drudge Report, CNN, MSNBC, CNBC, Breitbart
#   Will do unique checks depending on the site, example red text on Drudge, "Breaking News" on CNN, MSNBC etc
#   Otherwise will return top headlines


import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def DrudgeScrape():
  #full page screenshot generator
  driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1']) # or add to your PATH
  driver.get('https://www.drudgereport.com/')
  driver.save_screenshot("FullPage_Screenshot.png")

  #headline - Acquires top story, checks if "red", prints status based on color
  req = requests.get('http://www.drudgereport.com')
  soup = BeautifulSoup(req.content, 'html.parser')
  div = soup.find(id="app_mainheadline")
  stringed = str(div)
  RedHeadLine = div.find_all("font", attrs={'color': 'red'})
  if RedHeadLine:
      print("Important Front Page Story:\n"+div.get_text().strip()+"\n")
  else:
      print("Front Page Story: " + div.get_text())

  #redlines - Checks the rest of the stories for "red" status, prints matches
  print("Here are the rest of the red-status headlines:")
  div2 = soup.find_all("font", attrs={'color': 'red'})
  for i in div2:
      otherheadlines = i.get_text().strip()
      if str(otherheadlines) != str(div.get_text().strip()):
          print(i.get_text().strip()+"\n")

def CnnScrape():
  #full page screenshot generator
  driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1']) # or add to your PATH
  driver.get('https://www.cnn.com/')
  driver.save_screenshot("CNN_Screenshot.png")

  req = requests.get('http://www.cnn.com')
  soup = BeautifulSoup(req.content, 'html.parser')
  #check for breaking news
  
def MsnbcScrape():
  #full page screenshot generator
  driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1']) # or add to your PATH
  driver.get('https://www.msnbc.com/')
  driver.save_screenshot("MSNBC_Screenshot.png")

  req = requests.get('http://www.msnbc.com')
  soup = BeautifulSoup(req.content, 'html.parser')
  #check for breaking news
  
def BreitbartScrape():
  #full page screenshot generator
  driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1']) # or add to your PATH
  driver.get('https://www.breitbart.com/')
  driver.save_screenshot("Breitbart_Screenshot.png")

  req = requests.get('http://www.breitbart.com')
  soup = BeautifulSoup(req.content, 'html.parser')
