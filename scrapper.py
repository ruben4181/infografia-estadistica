from selenium import webdriver
from datetime import datetime, timedelta
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from time import sleep

def loadDriver():
    try:
        chrome_options = Options()
        #chrome_options.add_argument("--headless")
        #chrome_options.add_argument("--no-sandbox")
        #chrome_options.add_argument("disable-gpu")
        chrome_options.add_argument("window-size=1500, 700")
        chrome_options.add_argument("--user-data-dir=./infografia_profile")
        driver = webdriver.Chrome(executable_path='./drivers/chromedriver', options=chrome_options)       
        #driver = webdriver.Firefox()
        driver.get("https://www.twitter.com")
        print("Driver cargado")
        sleep(10)
        return driver
    except KeyboardInterrupt:
        exit()
        x=1/0
    except Exception as e:
        print("Error while initializing driver")
        print(e)
        x=1/0
        return []
	
def search(driver, searchInput, first):
	xpath1 = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/label/div[2]/div/input'
	xpath2 = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/form/div[1]/div/label/div[2]/div/input'
	toUse = xpath1
	if(not first):
		toUse = xpath2
	si = driver.find_elements_by_xpath(toUse)
	elems = len(si)
	if(elems>0):
		si = si[0]
		si.click()
		sleep(1)
		if(not first):
			clearButton = driver.find_elements_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/form/div[1]/div/label/div[3]/div/div')
			if(len(clearButton)>0):
				clearButton[0].click()
		si.clear()
		si.send_keys(searchInput)
		si.send_keys(Keys.RETURN)
		
	peopleIFollow = driver.find_elements_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div[2]/div[1]/div[1]/div/label[3]')
	elems = len(peopleIFollow)
	if(elems>0):
		peopleIFollow=peopleIFollow[0]
		peopleIFollow.click()
		
def extractContent(driver):
	tweetContent = driver.find_elements_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div[3]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div')
	elems = len(tweetContent)
	if(elems>0):
		tweetContent = tweetContent[0]
		lines = tweetContent.text.split("\n")
		saveInfo(lines)

def saveInfo(lines):
	rc = 0
	nc = 0
	deaths = 0
	m = 0
	
	for l in lines[0:7]:
		ss = l.split(" ")
		if(len(ss)>1):
			if("recuperados" in ss[1].lower()):
				rc=int(ss[0].replace(".", ""))
			elif("nuevos" in ss[1].lower()):
				nc=int(ss[0].replace(".", ""))
			elif("fallecidos" in ss[1].lower()):
				deaths = int(ss[0].replace(".", ""))
			elif("muestras" in ss[1].lower()):
				m = int(ss[0].replace(".", ""))
	print(str(rc)+","+str(nc)+","+str(deaths)+","+str(m))
	
def main():
	firstDay = {"year":2020, "month":6, "day":15}
	lastDay = {"year":2021, "month":6, "day":14}
	monthNames = ["void", "enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto",  "septiembre", "octubre", "noviembre", "diciembre"]
	
	actualDate = datetime(firstDay["year"], firstDay["month"], firstDay["day"]);
	lastDate = datetime(lastDay["year"], lastDay["month"], lastDay["day"]);
	searchInput = "#ReporteCovid19 "+str(actualDate.day)+" de "+monthNames[actualDate.month]

	driver = loadDriver()
	sleep(2)
	i=0
	while(actualDate<lastDate):
		"""if i==0:
			search(driver, searchInput, True)
		else:
			search(driver, searchInput, False)
		sleep(2)
		extractContent(driver)
		sleep(2)"""
		print(str(actualDate.year)+"/"+str(actualDate.month)+"/"+str(actualDate.day))
		actualDate = actualDate+timedelta(days=1)
		searchInput = "#ReporteCovid19 "+str(actualDate.day)+" de "+monthNames[actualDate.month]
		i+=1

main()
