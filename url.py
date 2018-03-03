#import requests
import urllib.parse
import urllib.request
#from bs4 import BeautifulSoup

'''
@args
    venue - The food venue to search
    time - The time of day to search (Breakfast/Lunch)
    date - The date of
'''
def parse_url(venue, time, date):
    url = "https://cafes.compass-usa.com/StonyBrook/SitePages/Menu.aspx?lid=a1"
    values = {"venueFilter": venue, "periodFilter": time, "datepicker-stonybrook": date}
    #data = requests.post(url, payload)
    payload = urllib.parse.urlencode(values)
    payload = payload.encode("ascii")
    data = urllib.request.Request(url , payload)
    with urllib.request.urlopen(data) as response:
        page = response.read()

if __name__ == "__main__":
    parse_url("Admin Cart", "Breakfast", "03/02/2018")
