import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def read_data():
    animals_data = load_data('animals_data.json')
    output = ""

    for animal in animals_data:
        output += "<li class='cards__item'>"

        if animal["name"]:
            output += f"\n<div class='card__title'>{animal["name"]}</div>"

        output += "<p class ='card__text'>"

        if animal["characteristics"]["diet"]:
            output += f"<strong>Diet:</strong> {animal["characteristics"]["diet"]}<br/>\n"

        if animal["locations"][0]:
            output += f"<strong>Location</strong>: {animal["locations"][0]}<br/>\n"

        if "type" in animal["characteristics"].keys():
            output += f"<strong>Type</strong>: {animal["characteristics"]["type"]}<br/>\n"

        output += "</p>"
        output += "</li>\n"

    return output


def replace_animals_info():
    with open("animals_template.html", "r") as f:
        html_script = f.read()
    animals_data = read_data()
    html_script_with_data = html_script.replace("__REPLACE_ANIMALS_INFO__", animals_data)
    return html_script_with_data


def write_data(script):
    with open("animals.html", "w") as f:
        f.write(script)

write_data(replace_animals_info())