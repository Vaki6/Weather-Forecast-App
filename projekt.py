import requests
from datetime import datetime
import json

API_KEY = '10e79b96f6a848729047763c246f3c4d'
URL = 'https://api.openweathermap.org/data/2.5/weather'


def idojaras_lekeres(varos):
    params = {
        'q': varos,
        'appid':API_KEY,
        'units': 'metric'
    }
    response = requests.get(URL, params = params)
    print(response.status_code)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def idojaras_megjelenitese(adat):
    varos = adat['name']
    homerseklet = adat['main']['temp']
    paratartalom = adat['main']['humidity']
    leiras = adat['weather'][0]['description']

    return f'{datetime.now()} | {varos} | {homerseklet}°C | {paratartalom}% | {leiras}'

def naplo_mentese(bejegyzes):
    with open('naplo.txt', 'a', encoding='UTF-8') as file:
        file.write(bejegyzes + '\n')


def naplo_megtekintese():
    try:
        with open('naplo.txt', 'r', encoding='UTF-8') as file:
            tartalom = file.read()
            if tartalom:
                print(tartalom)
            else:
                print('A napló üres')

    except FileNotFoundError:
        print('Nem létezik naplófájl!')

def menu():
    while True:
        print('\n Időjárás napló!')
        print('1. Időjárás lekérdezése')
        print('2. A napló megtekintése')
        print('3. Kilépés')
        valasztas = input('Válassz a lehetőségek közül (1-3): ')

        if valasztas == '1':
            varos = input('Add meg a város nevét: ').strip().lower()
            adat = idojaras_lekeres(varos)
            if adat:
                bejegyzes = idojaras_megjelenitese(adat)
                naplo_mentese(bejegyzes)

        elif valasztas == '2':
            naplo_megtekintese()

        elif valasztas == '3':
            print('Kilépés')
            break

        else:
            print('Érvénytelen választás! Kérlek probáld újra!')

if __name__ == '__main__':
    menu()



