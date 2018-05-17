#   Scraper and aggregator, will scrape top headlines for a series of websites from top contributors 
#   Top contributors will be sourced from a variety of viewpoints
#   Ex. Drudge Report, CNN, MSNBC, CNBC, Breitbart
#   Will do unique checks depending on the site, example red text on Drudge, "Breaking News" on CNN, MSNBC etc
#   Otherwise will return top headlines

import requests
from lxml import html
from PIL import ImageTk
from bs4 import BeautifulSoup
from selenium import webdriver
import tkinter


def popupgif(headline, happeningStatus):
    # create the canvas, size in pixels
    canvas = tkinter.Canvas(width=450, height=300, bg='black')
    canvas.pack(expand=tkinter.YES, fill=tkinter.BOTH)
    if happeningStatus:
        gifH = tkinter.PhotoImage(file='#path to image')
        canvas.create_image(50, 10, image=gifH, anchor=tkinter.NW)
        headtext = canvas.create_text(70, 10, text=headline, anchor='nw', font=("Times New Roman", 10, 'bold'),
                                      fill='red')
        canvas.insert(headtext, 12, "")
        tkinter.mainloop()
    else:
        canvas.image = ImageTk.PhotoImage(file='#path to image')
        canvas.create_image(50, 10, image=canvas.image, anchor=tkinter.NW)
        headtext = canvas.create_text(70, 10, text=headline, anchor='nw', font=("Times New Roman", 10, 'bold'),
                                      fill='white')
        canvas.insert(headtext, 12, "")
        tkinter.mainloop()


def DrudgeScrape():
    # headline
    req = requests.get('http://www.drudgereport.com')
    soup = BeautifulSoup(req.content, 'html.parser')
    div = soup.find(id="app_mainheadline")
    topheadline = div.find_all("font", attrs={'color': 'red'})
    if topheadline:
        happening = True
        print("IT'S HAPPENING!\n" + div.get_text().strip() + "\n")
        popupgif(div.get_text().strip(), happening);
    else:
        happening = False
        print("It's NOT happening, but here is the top headline anyway:\n" + div.get_text() + "\n")
        popupgif(div.get_text().strip(), happening);
    # redlines
    print("Here are the rest of the red-status headlines:")
    div2 = soup.find_all("font", attrs={'color': 'red'})
    for i in div2:
        otherheadlines = i.get_text().strip()
        if str(otherheadlines) != str(div.get_text().strip()):
            print(i.get_text().strip() + "\n")


def CnnScrape():
    # full page screenshot generator
    driver = webdriver.PhantomJS(
        service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])  # or add to your PATH
    driver.get('https://www.cnn.com/')
    driver.save_screenshot("CNN_Screenshot.png")
    #soup = BeautifulSoup(resp.text, 'lxml')
    req = requests.get('http://www.cnn.com')
    soup = BeautifulSoup(req.content, 'html.parser')
    print(soup)
    # check for breaking news


def MsnbcScrape():
    # full page screenshot generator
    driver = webdriver.PhantomJS(
        service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])  # or add to your PATH
    driver.get('https://www.msnbc.com/')
    driver.save_screenshot("MSNBC_Screenshot.png")

    req = requests.get('http://www.msnbc.com')
    tree = html.fromstring(req.content)
    # check for breaking news
    headlines = 5
    for each in range(headlines):
        topHeadlines = tree.xpath('// *[ @ id = "block-system-main"] / div / div / div / div / div[3] \
                                                      / div / div / div / aside / div / div[1] / ul / \
                                                           li['+str(each+1)+'] / a / span[2] / text()')
        print(topHeadlines)

def BreitbartScrape():
    # full page screenshot generator
    driver = webdriver.PhantomJS(
        service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])  # or add to your PATH
    driver.get('https://www.breitbart.com/')
    driver.save_screenshot("Breitbart_Screenshot.png")

    req = requests.get('http://www.breitbart.com')
