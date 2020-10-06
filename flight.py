from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")      #Give the path to chromedriver
driver.get("https://www.makemytrip.com/")

n = input("Enter Confirmation ")            #Type anything after complete loading of the website.

path = '//*[@id="root"]/div/div[2]/div/div/div[2]'
driver.find_element_by_xpath(path).click()                  #opening destination list

sleep(5)

path2 = '//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div/input'
driver.find_element_by_xpath(path2).send_keys('TRV')        #Trivandrum, India

sleep(5)

path3 = '//*[@id="react-autowhatever-1"]/div[1]'
driver.find_element_by_xpath(path3).click()                 #Selection City

sleep(5)

path4 = '//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[3]/div[3]/div[6]'
driver.find_element_by_xpath(path4).click()                 #Date Selection

sleep(5)

path5 = '//*[@id="root"]/div/div[2]/div/div/div[2]/p/a'
driver.find_element_by_xpath(path5).click()                 #Submit Button

sleep(5)

path6 = '//*[@id="sorting-togglers"]/div[5]/span'
driver.find_element_by_xpath(path6).click()                 #Select Price Descending order

sleep(10)

flight = []

content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")

name = []
DeptTime = []
ArrTime = []
cost = []

count = 0

if soup.findAll('div', attrs={'class': 'one-way'}):
    for a in soup.findAll('span', attrs={'class': 'airways-name'}):
        count = count + 1
        name.append(a.get_text())
        if count == 5:
            break
    count = 0
    for a in soup.findAll('div', attrs={'class': 'dept-time'}):
        count = count + 1
        DeptTime.append(a.get_text())
        if count == 5:
            break
    count = 0
    for a in soup.findAll('p', attrs={'class': 'reaching-time append_bottom3'}):
        count = count + 1
        ArrTime.append(a.get_text())
        if count == 5:
            break
    count = 0
    for a in soup.findAll('span', attrs={'class': 'actual-price'}):
        count = count + 1
        cost.append(a.get_text())
        if count == 5:
            break

    print("NEXT")
else:
    print("NOPE")

for i in range(5):
    print("Flight no : "+str(i+1))
    print("Flight Name : "+name[i])
    print("Flight Departure Time : "+DeptTime[i])
    print("Flight Arrival Time : "+ArrTime[i])
    print("Flight Cost : "+cost[i])
    print()