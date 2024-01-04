import requests
import selectorlib


URL = "http://programmer100.pythonanywhere.com/tours/"



def scrape(URL):
    responce = requests.get(URL)
    source = responce.text
    return source


if __name__ == "__main__":
    print(scrape(URL))