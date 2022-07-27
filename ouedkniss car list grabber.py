from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import numpy

car_link_list = []
car_name_list = []
car_category_list = []
car_energie_list = []
car_moteur_list = []
car_transmission_list = []
car_kilometrage_list = []
car_couleur_list = []
car_papiers_list = []
car_options_list = []
car_OPTIONS_list = []


def car_link_grab(web_link):
    source = urllib.request.urlopen(
        f"{web_link}").read()
    soup = BeautifulSoup(source, "lxml")
    car_desc = soup.find_all("span", class_="annonce_get_description")
    car_links = soup.find_all("a", class_="d-flex flex-column flex-grow-1 v-card v-card--link v-sheet theme--dark")

    for car_link in car_links:
        car_link_list.append("https://www.ouedkniss.com/"+car_link.a["href"])


def car_name_grab():
    for link in car_link_list:
        source = urllib.request.urlopen(f"{link}").read()
        soup = BeautifulSoup(source, "lxml")
        car_name = soup.find("h1", id="Title")
        if car_name:
            car_name_list.append(car_name.text)
        else:
            car_name_list.append("NaN")


def car_features():
    for link in car_link_list:
        source = urllib.request.urlopen(f"{link}").read()
        soup = BeautifulSoup(source, "lxml")

        car_category = soup.find("p", id="Catégorie")
        if car_category:
            car_category_list.append(car_category.text)
        else:
            car_category_list.append("NaN")
        car_energie = soup.find("p", id="Energie")
        if car_energie:
            car_energie_list.append(car_energie.text)
        else:
            car_energie_list.append("NaN")
        car_moteur = soup.find("p", id="Moteur")
        if car_moteur:
            car_moteur_list.append(car_moteur.text)
        else:
            car_moteur_list.append("NaN")
        car_transmission = soup.find("p", id="Transmission")
        if car_transmission:
            car_transmission_list.append(car_transmission.text)
        else:
            car_transmission_list.append("NaN")
        car_kilometrage = soup.find("p", id="Kilométrage")
        if car_kilometrage:
            car_kilometrage_list.append(car_kilometrage.text)
        else:
            car_kilometrage_list.append("NaN")
        car_couleur = soup.find("p", id="Couleur")
        if car_couleur:
            car_couleur_list.append(car_couleur.text)
        else:
            car_couleur_list.append("NaN")
        car_papiers = soup.find("p", id="Papiers")
        if car_papiers:
            car_papiers_list.append(car_papiers.text)
        else:
            car_papiers_list.append("NaN")
        car_options = soup.find("p", id="Options")
        if car_options:
            car_options_list.append(car_options.text)
        else:
            car_options_list.append("NaN")
        car_OPTIONS = soup.find("div", id="options")
        if car_OPTIONS:
            car_OPTIONS_list.append(car_OPTIONS.text)
        else:
            car_OPTIONS_list.append("NaN")


link = input("Web Site link: ")

car_link_grab(link)
car_features()
car_name_grab()

dict = {
    "Vechile": car_name_list,
    "Category": car_category_list,
    "Engine": car_energie_list,
    "Moteur": car_moteur_list,
    "Transmission": car_transmission_list,
    "Kilométrage": car_kilometrage_list,
    "Couleur": car_couleur_list,
    "Papiers": car_papiers_list,
    "Options": car_options_list,
    "OPTIONS": car_OPTIONS_list,
}
df = pd.DataFrame(dict)
df = df.fillna({"OPTIONS": "No Discription", "Options": "No Discription"})
df = df.dropna()
df = df.replace({
    "Category": "Type du véhicule :",
    "Engine": "Energie :",
    "Moteur": "Moteur :",
    "Transmission": "Transmission :",
    "Kilométrage": "Kilométrage :",
    "Couleur": "Couleur :",
    "Papiers": "Papiers :",
    "Options": "Options :",
}, "", regex=True)
source = urllib.request.urlopen(link).read()
soup = BeautifulSoup(source, "lxml")
title = soup.title.text
df.to_csv(f"{title}.csv", index=False)
