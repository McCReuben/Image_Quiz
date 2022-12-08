import os
from serpapi import GoogleSearch

API_key = os.getenv("SERP_API_KEY")
API_key = "5074028568879874a7f573b4071fb9c484bf3e91e883b98d94949d6298b85f86"

possible_search_terms = ["TEM","SEM","XRD","XRF","XANES"]

def generate_microscope_search_params(microscope):
    params = {
        "q": "Images from a {}""".format(microscope),
        "tbm": "isch",
        "ijn": "0",
        "api_key": API_key
    }
    return params

search = GoogleSearch(generate_microscope_search_params(possible_search_terms[1]))
results = search.get_dict()
images_results = results["images_results"]


print(images_results)