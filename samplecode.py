from bs4 import BeautifulSoup
import bs4
from selenium import webdriver
import time

browser=webdriver.Firefox()

#getting the browser of selenium
browser.get("https://www.zomato.com/ahmedabad")
page=None
soup=None
#This is for the serchbox id of the zomato
search = browser.find_element_by_id("keywords_input")
search.send_keys('McDonald')
time.sleep(5)
search.send_keys(Keys.RETURN)
time.sleep(5)
try:
		browser.find_element_by_xpath("//a[@class='ui ta-right pt10 fontsize3 zred pb10 pr10']")
	except:
		pass
page = browser.page_source
soup = BeautifulSoup(page,"lxml")
name_dict={}
count=0
new = soup.find_all("a",attrs={'data-result-type':'ResCard_Name'})
if(len(new) == 0 ):
	new = soup.find_all("a",attrs={'class':'ui large header left'})
for tag in new:
	count +=1
	if(tag.get_text().strip() == user_input):
		name_dict.update({count:{"name":tag.text.strip(),"link":tag['href'].strip()}})
print(name_dict)
review_dict= {}
count = 0
for x in name_dict:
	count += 1
	browser.get(name_dict[x]['link'])
	try:
			#this for all review class disply
		browser.find_element_by_xpath("//a[@data-sort='reviews-dd']").click()
		while True:
			try:	#this is for find loadmore
				browser.find_element_by_xpath("//div[@class='load-more bold ttupper tac cursor-pointer fontsize2']").click()
			except:
				break
	except:
		break
	page = browser.page_source
	soup = BeautifulSoup(page,"lxml")
	review = []
	for tag in soup.find_all("div", attrs= {"class":"rev-text mbot0 "}):
		review.append(tag.get_text().strip())
	review_dict.update({count:{"name":soup.find("a",{"class":"ui large header left"}).text.strip(),"area":soup.find("a",{"class":"left grey-text fontsize3"}).text.strip(),"review":review}})

	
