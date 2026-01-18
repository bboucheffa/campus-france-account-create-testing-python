import json
from model.personne import personne

def read_data_from_json(file_path="data/Personnes.json"):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    personnes = [personne(**e) for e in data]
    return personnes