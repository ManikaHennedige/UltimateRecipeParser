from recipe_scrapers import scrape_me
from ingredientparser import parseIngredients
import os
import json
import logging
logging.basicConfig(filename='example.log', level=logging.DEBUG) # set up logging

vulgar_to_float = {
    "\u00BC": 1.0 / 4.0,
    "\u00BD": 1.0 / 2.0,
    "\u00BE": 3.0 / 4.0,
    "\u2150": 1.0 / 7.0,
    "\u2151": 1.0 / 9.0,
    "\u2152": 1.0 / 10.0,
    "\u2153": 1.0 / 3.0,
    "\u2154": 2.0 / 3.0,
    "\u2155": 1.0 / 5.0,
    "\u2156": 2.0 / 5.0,
    "\u2157": 3.0 / 5.0,
    "\u2158": 4.0 / 5.0,
    "\u2159": 1.0 / 6.0,
    "\u215A": 5.0 / 6.0,
    "\u215B": 1.0 / 8.0,
    "\u215C": 3.0 / 8.0,
    "\u215D": 5.0 / 8.0,
    "\u215E": 7.0 / 8.0,
    "\u2189": 0.0 / 3.0,
}
# exception friendly parser to attempt to get all attributes from the scraper object
def RecipeParser(siteParser):
    recipeData = {}
    try:
        title = siteParser.title()
        recipeData["title"] = title
    except Exception:
        logging.warning("Failed to parse title")
    try:
        total_time = siteParser.total_time()
        recipeData["total_time"] = total_time
    except Exception:
        logging.warning("Failed to parse total time")

    try:
        yields = siteParser.yields()
        recipeData["yield"] = yields
    except Exception:
        logging.warning("Failed to parse yield")

    try:
        ingredients = siteParser.ingredients()
        # print(ingredients)
        cleanedIngredients = list()

        for ingredient in ingredients:
            ingredientWords = list()
            for word in ingredient.split(" "):
                if word in vulgar_to_float.keys():
                    ingredientWords.append(str(vulgar_to_float[word]))
                else:
                    ingredientWords.append(word)
            cleanedIngredients.append(' '.join(ingredientWords))
        recipeData["ingredients"] = parseIngredients(cleanedIngredients)
    except Exception:
        logging.warning("Failed to parse ingredient list")

    try:
        instructions = siteParser.instructions()
        directions = instructions.split('\n')
        recipeData["instructions"] = directions
    except Exception:
        logging.warning("Failed to parse instructions")

    try:
        image = siteParser.image()
        recipeData["image"] = image
    except Exception:
        logging.warning("Failed to parse image")

    try:
        prep_time = siteParser.prep_time()
        recipeData["prep_time"] = prep_time
    except Exception:
        logging.warning("Failed to parse prep time")

    try:
        cook_time = siteParser.cook_time()
        recipeData['cook_time'] = cook_time
    except Exception:
        logging.warning("Failed to parse cook time")

    try:
        ratings = siteParser.ratings()
        recipeData["ratings"] = ratings
    except Exception:
        logging.warning("Failed to parse ratings")

    try:
        nutrients = siteParser.nutrients()
        recipeData["nutrients"] = nutrients
    except Exception:
        logging.warning("Failed to parse nutrients")

    try:
        url = siteParser.url
        recipeData["url"] = url
    except Exception:
        logging.warning("Failed to parse URL")

    return recipeData


count = 0
# get all the recipes from the RecipePathLast (which contains only files with URLs)
with open("RecipeListPath.txt", "r") as f:
    for recipePath in f.readlines():
        recipePath = recipePath[:-1]
        if os.stat(recipePath).st_size != 0:  # check if empty file
            with open(recipePath,) as recipeFile:
                data = json.load(recipeFile)
                url = data["url"] # get url address from the file
                count += 1
            with open("testrecipefile.json", "w+") as writingFile: # change to recipePath to replace the actual file
                try:
                    scraper = scrape_me(url)  # sometimes, the scraper might not support a website
                    recipeContents = RecipeParser(scraper)
                except Exception:
                    recipeContents = {}
                # dump the contents into the original json file
                # if the url from the file is unable to be parsed by the parser, the file is completely wiped
                # will need to implement a check to make sure resulting files aren't empty before use
                json.dump(recipeContents, writingFile, indent=4)
                print(count)
                break  # stop after 1 iteration

print("finished: ", count)

