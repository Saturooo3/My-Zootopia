import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

for animal in animals_data:
    if animal["name"]:
        name = animal["name"]
        print(f"\nName: {name}")

    if animal["locations"][0]:
        location = animal["locations"][0]
        print(f"Location: {location}")

    if animal["characteristics"]["diet"]:
        diet = animal["characteristics"]["diet"]
        print(f"Diet: {diet}")

    if 'type' in animal["characteristics"].keys():
        animal_type = animal["characteristics"]["type"]
        print(f"Type: {animal_type}")



