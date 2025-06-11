#import os

#def tracker():
    #current_path = os.getcwd()
    #modules used
    #import datetime
    #import phonenumbers
    #from phonenumbers import geocoder
    #import folium
    #from phonenumbers import carrier
    #from opencage.geocoder import OpenCageGeocode

    #num = input("Enter a number: ")
    #time_ = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    #API key
    #API_key = "_OPEN_CAGE_GEOCODE_API_KEY_"
    #sanNummber = phonenumbers.parse(num)
    #country Location finder
    #location = geocoder.description_for_number(sanNummber,"en")
    #Service provider finder
   # sea_pro = phonenumbers.parse(num)
   # servise_prover=carrier.name_for_number(sea_pro,'en')
    #Finding the latitude and longitude
    #geocoder = OpenCageGeocode(API_key)
    #quesry = str(location)
    #resltt = geocoder.geocode(quesry)
    #lat = resltt[0]['geometry']['lat']
    #lng = resltt[0]['geometry']['lng']
    #creating a map with the phone number location as pointer
    #mymap = folium.Map(location=[lat,lng],zoom_start=9)
   # folium.Marker([lat,lng],popup=location).add_to(mymap)
  #  mymap.save(rf"{current_path}/Maps/{num+str('-')+str(time_)}.html")
##
   # return location,servise_prover,lat,lng
#api_key=
import requests
from pathlib import Path
import datetime
import folium

def tracker():
    current_path = Path.cwd()
    time_ = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    num = input("Enter phone number with country code (e.g., +): ")

    # Use NumVerify API
    API_KEY = ""#use your own api key
    url = f"http://apilayer.net/api/validate?access_key={API_KEY}&number={num}"
    
    try:
        response = requests.get(url)
        data = response.json()

        if data.get('valid'):
            location = data.get('location', 'Unknown')
            carrier = data.get('carrier', 'Unknown')

            print("Number:", data.get('international_format'))
            print("Country:", data.get('country_name'))
            print("Location:", location)
            print("Carrier:", carrier)
            print("Line Type:", data.get('line_type'))

            lat, lng = None, None

            if location:
                try:
                    # OPTIONAL: Only if OpenCage is set up
                    from opencage.geocoder import OpenCageGeocode
                    open_cage_key = "_OPEN_CAGE_GEOCODE_API_KEY_"
                    geocoder = OpenCageGeocode(open_cage_key)
                    query = f"{location}, {data.get('country_name', '')}"
                    result = geocoder.geocode(query)

                    if result:
                        lat = result[0]['geometry']['lat']
                        lng = result[0]['geometry']['lng']

                        # Create map
                        mymap = folium.Map(location=[lat, lng], zoom_start=9)
                        folium.Marker([lat, lng], popup=query).add_to(mymap)
                        map_path = current_path / "Maps" / f"{num}-{time_}.html"
                        map_path.parent.mkdir(parents=True, exist_ok=True)
                        mymap.save(map_path)
                        print(f"Map saved to: {map_path}")
                except Exception as geo_err:
                    print("Geocoding failed:", geo_err)

            return location, carrier, lat, lng
        else:
            print("Invalid phone number.")
            return None, None, None, None

    except Exception as e:
        print("Tracker error:", e)
        return None, None, None, None
