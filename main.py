import requests
import selectorlib


URL = "http://programmer100.pythonanywhere.com/tours/"
URL1 = "https://service.berlin.de/terminvereinbarung/termin/taken/#&termin=1&dienstleister=327437&anliegen[]=120691"


def scrape(URL):
    responce = requests.get(URL)
    source = responce.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value


if __name__ == "__main__":
    source = scrape(URL)
    result = extract(source)
    print(result)
