import requests
import selectorlib
import os
import smtplib, ssl


URL = "http://programmer100.pythonanywhere.com/tours/"

if not os.path.exists("data.txt"):
    with open("data.txt", "w") as file:
        pass


def scrape(URL):
    responce = requests.get(URL)
    source = responce.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value




def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "ibrohimovmuhammad2020@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "ibrohimovmuhammad2020@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port,context= context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)



def save_data(result):
    with open("data.txt", "a") as file:
        file.write(result + "\n")


if __name__ == "__main__":
    source = scrape(URL)
    result = extract(source)
    print(result)
    if result != "No upcoming tours":
        if result not in "data.txt":
            send_email(message="Hey, new slot was found")
            save_data(result)
