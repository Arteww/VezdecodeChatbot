import os
from json import load

path_to_pictures_json = f'{os.path.dirname(os.path.abspath(__file__))}/cards.json'

with open(path_to_pictures_json, 'r', encoding="utf-8") as file:
    cards = load(file)
