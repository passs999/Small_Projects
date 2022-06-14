from bs4 import BeautifulSoup
import requests
import time

def weather_scraper():
    print(5 * '_--_', "Weather Scraper", 5 * '_--_', '\n')
    country = str(input("Enter Country --> "))
    city = str(input("Enter City --> "))
    city = city.replace(" ", "")
    
    
    if country == '':
        print("You must enter the country")
        print(15 * '_-')
        weather_scraper()
    if city == '':
        print("You must enter the city")
        print(15 * '_-')
        weather_scraper()
        
    try:
        url = 'https://www.timeanddate.com/weather/{}/{}'
        page = requests.get((url.format(country, city)))
        doc = BeautifulSoup(page.text, "html.parser")
        
        
        #scraping location
        location = doc.find_all(class_="table table--left table--inner-borders-rows")
        location = location[0].parent
        location = location.find("td")
        location = (location.string)
    
        
        #scraping temperature
        temperature = doc.find(class_="h2")
        temperature = (temperature.string)
    
        
        #scraping weather
        weather = doc.find_all(class_=("bk-focus__qlook"))
        weather = doc.find("p")
        weather = (weather.string)
        weather = weather.replace(".","")
        
        
        #scraping time
        time = doc.find(id="wtct")
        time = (time.string)
        
        
        #print answer
        print(15 * '__')
        print("Location:", location)
        print("Temperature:", temperature)
        print("Weather:", weather)
        print(time)
        print(15 * '__')
    
        retry = input("If you want to exit enter -> e\nIf you want to retry enter -> r\n-->")
        if retry == 'e':
            exit()
        if retry == 'r':
            weather_scraper()
        else:
            quit()
        

    except KeyboardInterrupt:
        print("Country or city entered wrong, try again")
        print(15 * '__')
        weather_scraper()
    except IndexError:
        print("Country or city entered wrong, try again")
        print(15 * '__')
        weather_scraper()
    
weather_scraper()
