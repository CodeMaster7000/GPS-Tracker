from selenium import webdriver
import folium
import datetime
import requests
import time

def locationCoordinates():
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        loc = data['loc'].split(',')
        lat, long = float(loc[0]), float(loc[1])
        city = data.get('city', 'Unknown')
        state = data.get('region', 'Unknown')
        return lat, long, city, state
      
    except:
        print("Internet unavailable.")
        exit()
        return False

def gps_locator():
    obj = folium.Map(location=[0, 0], zoom_start=2)
    try:
        lat, long, city, state = locationCoordinates()
        print("You are in {},{}".format(city, state))
        print("Your latitude: {} and longitude = {}".format(lat, long))
        folium.Marker([lat, long], popup='Current location:').add_to(obj)
        fileName = "C:/screengfg/Location" + \
            str(datetime.date.today()) + ".html"
        obj.save(fileName)
        return fileName
      
    except:
        return False

if __name__ == "__main__":
    print(" GPS Tracker \n")
    page = gps_locator()
    print("\nOpening file...")
    dr = webdriver.Chrome()
    dr.get(page)
    time.sleep(4)
    dr.quit()
    print("\nThe browser is closed.")
