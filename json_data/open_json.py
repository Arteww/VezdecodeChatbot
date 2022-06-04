import os
from json import load, dump

from vkbottle.modules import json

path_to_pictures_json = f'{os.path.dirname(os.path.abspath(__file__))}\cards.json'

with open(path_to_pictures_json, 'r', encoding="utf-8") as file:
    cards = load(file)

data = {}
for i in cards:
    data[i] = str(cards[i]).split()
with open("cards.json", "w", encoding="utf-8") as file:
    dump(data, file, indent=3, ensure_ascii=False)
