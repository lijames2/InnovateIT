#import requests
#import urllib.parse
#import urllib.request
#from bs4 import BeautifulSoup

'''
@args
    venue - The food venue to search
    time - The time of day to search (Breakfast/Lunch)
    date - The date of
'''
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
'''
def get_url_data(place, date, time):
    valid_times = ["Breakfast", "Brunch", "Lunch", "Dinner", "Midnight"]
    append = False
    results = ""
    if place == "East Side Dine-In":
        with open("east-dining.txt") as f:
            lines = f.readlines()
            for i in range(0, len(lines)):
                items = lines[i].split()
                if len(items) == 1 and lines[i].strip() in valid_times and lines[i].strip() != time:
                    append = False
                if append:
                    if len(items) == 2:
                        results += items[0] + " Calories: %d" %int(items[1]) + "\n"
                    else:
                        results += " ".join(items[0: len(items) - 1]) + ", Calories: %d" %int(items[len(items) - 1]) + "\n"
                if lines[i].strip() == time:
                    append = True
    elif place == "West Side Dine-In":
        with open("west-dining.txt") as f:
            lines = f.readlines()
            for i in range(0, len(lines)):
                items = lines[i].split()
                if len(items) == 1 and lines[i].strip() in valid_times and lines[i].strip() != time:
                    append = False
                if append:
                    results += " ".join(items[0: len(items) - 1]) + ", Calories: %d" %int(items[len(items) - 1]) + "\n"
                if lines[i].strip() == time:
                    append = True
    if len(results) > 0:
        return results
    return "Sorry, we did not find any results for that :("

if __name__ == "__main__":
    #parse_url("East Side Dine-In", "Breakfast", "03/02/2018")
    #valid_times = ["Breakfast", "Brunch", "Lunch", "Dinner", "Midnight"]
    print(get_url_data("East Side Dine-In", "03/03/2018", "Midnight"))
