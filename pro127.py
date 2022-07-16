import csv
import time
import requests 
from bs4 import BeautifulSoup

start_url="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser=requests.Chrome("C:\WHITEHAT 26-7-21\Python\chromedriver.exe",verify=False)

browser.get(start_url)
time.sleep(15)

def scrap():
    headers=["Name","Distance","Mass","Radius"]
    star_data=[]
    for i in range(0,102):
        soup=BeautifulSoup(browser.page_source,"html.parser")
        for th_tag in soup.find_all("th",attrs={"class","headerSort"}):
            tr_tags=th_tag.find_all("tr")
            templist=[]
            for index,tr_tag in enumerate(tr_tags):
                if index==0:
                    templist.append(tr_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        templist.append(tr_tag.contents[0])
                    except:
                        templist.append("")
            star_data.append(templist)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("Planets.csv","w") as f:
        csvwriter=csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(star_data)


scrap()