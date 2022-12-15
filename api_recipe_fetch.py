import re
from urllib import response
import requests
import time
import json

def append_ingredients(url, input):
    ingredients = input.split(", ")
    for i in ingredients:
        url = url + i.replace(" ", "") + ",+"
    url = url.strip(",+")
    url = url + "&number=10"
    return url

def search_api(url):
    response = requests.get(url)
    resp = response.json()
    recipe_list = []
    for i in range(10):
        list = [resp[i]["title"], resp[i]["id"]]
        ing = resp[0]["missedIngredients"]
        for j in ing:
            list.append(j["name"])
        recipe_list.append(list)
    return recipe_list

def search_source_recipe(url_source, search_results):
    for i in search_results:
        url_source = url_source + str(i[1]) + ","
    url_source = url_source.strip(",")
    response = requests.get(url_source)
    resp = response.json()
    sources = []
    for j in resp:
        sources.append(j["sourceUrl"])
    return sources

def print_recipes(search_results, sources):
    for i in range(10):
        print("Recipe Name:", search_results[i][0])
        print("Extra Ingredients:", search_results[i][2:])
        print("Recipe Source:", sources[i])

input = str(input("Enter your ingredients separated by a comma and space like this ', ' : "))
# url = "https://api.spoonacular.com/recipes/findByIngredients?apiKey=e6eba09eeeb6468fa728b8e8fdbfb3da&addRecipeInformation=true&ingredients="
url = "https://api.spoonacular.com/recipes/findByIngredients?apiKey=e6eba09eeeb6468fa728b8e8fdbfb3da&ingredients="
url_source = "https://api.spoonacular.com/recipes/informationBulk?apiKey=e6eba09eeeb6468fa728b8e8fdbfb3da&ids="

url = append_ingredients(url, input)
search_results = search_api(url)
sources = search_source_recipe(url_source, search_results)

print_recipes(search_results, sources)