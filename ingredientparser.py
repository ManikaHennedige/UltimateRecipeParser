from ingredients import *
import json
import re

parenthesesRegex = re.compile(r"\([^()]*\)")
# load list of all ingredients
allIngredientsFile = open("allIngredients.txt", "r")
allIngredients = allIngredientsFile.read().split("\n")
allIngredientsFile.close()

while "" in allIngredients:
    allIngredients.remove("")

unlabeledIngredients = set()
unlabeledRecipes = set()


#
# function to parse all ingredients and their amounts, as well as determine a label for the recipe
# returns a list of json-formatted ingredients
#
def parseIngredients(ingredientList):
    #
    # get ingredients
    #
    # with open(recipeFilePath, ) as recipeFile:
    #     data = json.load(recipeFile)
    #     ingredientObjects = data["ingredients"]  # get url address from the file

    ingredientObjects = ingredientList
    count = len(ingredientObjects)
    ingredients = []
    for i in range(0, count):
        ingredientString = ingredientObjects[i]

        # check if not ingredient, but separator
        # ie "For Bread:"
        if ingredientString.find("For ") == 0 or " " not in ingredientString or \
                (":" in ingredientString and "eg:" not in ingredientString):
            continue

        ingredient = {}

        ingredient["descriptions"] = []

        # move parentheses to description
        while True:
            parentheses = parenthesesRegex.search(ingredientString)
            if not parentheses:
                break
            searchString = parentheses.group()
            ingredientString = ingredientString.replace(searchString, "")
            ingredient["descriptions"].append(searchString[1:-1])

        # remove "," and "-" then split ingredient into words
        ingredientString = ingredientString.replace(",", " and ")
        ingredientString = ingredientString.replace("-", " ")
        parsedIngredient = ingredientString.split(" ")

        # remove "", caused by extra spaces
        while "" in parsedIngredient:
            parsedIngredient.remove("")

        # move prepositions to description
        for index in range(0, len(parsedIngredient)):
            if parsedIngredient[index] in prepositions:
                if (index + 1 < len(parsedIngredient) and parsedIngredient[index + 1] == "use") or \
                        (index > 0 and parsedIngredient[index - 1] == "bone" and parsedIngredient[index] == "in"):
                    continue

                parsedPrepositionalPhrase = parsedIngredient[index:]
                ingredient["descriptions"].append(" ".join(parsedPrepositionalPhrase))
                parsedIngredient = parsedIngredient[:index]
                break

        #
        # get ingredient amount
        #

        ingredient["amount"] = 0
        while len(parsedIngredient) > 0:
            # check if current word is number of inches, not amount
            if len(parsedIngredient) > 1 and parsedIngredient[1] == "inch":
                break

            # get first word

            # if first word is digit or fraction, eval
            # "x" not multiplier, "%" used as modulo
            try:
                ingredient["amount"] += eval(parsedIngredient[0])
                del parsedIngredient[0]
            except (SyntaxError, NameError, TypeError):
                break

        #
        # get ingredient unit
        #

        # check words for unit
        unitString = ""
        for i in range(0, len(parsedIngredient)):
            pluralUnit = inCheckingPlurals(parsedIngredient[i], measurementUnits)
            if pluralUnit:
                unitString = pluralUnit
                del parsedIngredient[i]

                if i < len(parsedIngredient) and parsedIngredient[i] == "+":
                    while "+" in parsedIngredient:
                        index = parsedIngredient.index("+")
                        del parsedIngredient[index]
                        ingredient["amount"] += transformToCups(eval(parsedIngredient[index]), parsedIngredient[index + 1])
                        del parsedIngredient[index]
                        del parsedIngredient[index + 1]

                break

        # check for "cake" as unit, but only if "yeast" somewhere in ingredient
        if "yeast" in parsedIngredient:
            for word in parsedIngredient:
                if equalCheckingPlurals(word, "cakes"):
                    unitString = "cakes"
                    parsedIngredient.remove(word)
                    break

        # check if first word in array is "or", then ingredient has 2 possible units
        if parsedIngredient[0] == "or":
            pluralUnit = inCheckingPlurals(parsedIngredient[1], measurementUnits)
            if pluralUnit:
                unitString += " " + parsedIngredient[0] + " " + pluralUnit
                parsedIngredient = parsedIngredient[2:]

        # delete "of" at first index, ie "1 cup of milk" -> "1 cup milk"
        if parsedIngredient[0] == "of":
            del parsedIngredient[0]

        ingredient["unit"] = unitString

        #
        # get ingredient descriptions
        #

        # remove useless words
        for word in parsedIngredient:
            if word in unnecessaryDescriptions:
                parsedIngredient.remove(word)

        index = 0
        while index < len(parsedIngredient):
            descriptionString = ""
            word = parsedIngredient[index]

            # search through descriptions (adjectives)
            if word in descriptions:
                descriptionString = word

                # check previous word
                if index > 0:
                    previousWord = parsedIngredient[index - 1]
                    if previousWord in precedingAdverbs or previousWord[-2:] == "ly":
                        descriptionString = previousWord + " " + word
                        parsedIngredient.remove(previousWord)

                # check next word
                elif index + 1 < len(parsedIngredient):
                    nextWord = parsedIngredient[index + 1]
                    if nextWord in succeedingAdverbs or nextWord[-2:] == "ly":
                        descriptionString = word + " " + nextWord
                        parsedIngredient.remove(nextWord)

            # word not in descriptions, check if description with predecessor
            elif word in descriptionsWithPredecessor and index > 0:
                descriptionString = parsedIngredient[index - 1] + " " + word
                del parsedIngredient[index - 1]

            # either add description string to descriptions or check next word
            if descriptionString == "":
                index += 1
            else:
                ingredient["descriptions"].append(descriptionString)
                parsedIngredient.remove(word)

        # remove "and"
        while "and" in parsedIngredient:
            parsedIngredient.remove("and")

        # remove "style"
        while "style" in parsedIngredient:
            parsedIngredient.remove("style")

        # remove "or" if last word
        if parsedIngredient[-1] == "or":
            del parsedIngredient[-1]

        # replace hyphenated prefixes and suffixes
        for word in parsedIngredient:
            for hypenatedSuffix in hypenatedSuffixes:
                if hypenatedSuffix in word:
                    word = word.replace(hypenatedSuffix, "-" + hypenatedSuffix)

            for hypenatedPrefix in hypenatedPrefixes:
                if word.find(hypenatedPrefix) == 0:
                    word = word.replace(hypenatedPrefix, hypenatedPrefix + "-")

        # move various nouns to description
        if "powder" in parsedIngredient and \
                ("coffee" in parsedIngredient or \
                 "espresso" in parsedIngredient or \
                 "tea" in parsedIngredient):
            parsedIngredient.remove("powder")
            ingredient["descriptions"].append("unbrewed")

        #
        # get ingredient
        #
        ingredientString = " ".join(parsedIngredient)

        # remove "*", add footnote to description
        if "*" in ingredientString:
            ingredient["descriptions"].append("* see footnote")
            ingredientString = ingredientString.replace("*", "")

        # standardize "-" styling
        ingredientString = ingredientString.replace("- ", "-")
        ingredientString = ingredientString.replace(" -", "-")
        ingredientString = ingredientString.replace("Jell O", "Jell-O")
        ingredientString = ingredientString.replace("half half", "half-and-half")

        # remove unnecessary punctuation
        ingredientString = ingredientString.replace(".", "")
        ingredientString = ingredientString.replace(";", "")

        # fix spelling errors
        ingredientString = ingredientString.replace("linguini", "linguine")
        ingredientString = ingredientString.replace("filets", "fillets")
        ingredientString = ingredientString.replace("chile", "chili")
        ingredientString = ingredientString.replace("chiles", "chilis")
        ingredientString = ingredientString.replace("chilies", "chilis")
        ingredientString = ingredientString.replace("won ton", "wonton")
        ingredientString = ingredientString.replace("liquer", "liqueur")
        ingredientString = ingredientString.replace("confectioners ", "confectioners' ")
        ingredientString = ingredientString.replace("creme de cacao", "chocolate liquer")
        ingredientString = ingredientString.replace("pepperjack", "Pepper Jack")
        ingredientString = ingredientString.replace("Pepper jack", "Pepper Jack")
        ingredientString = ingredientString.replace("or more to taste", "")

        # standardize ingredient styling
        ingredientString = ingredientString.replace("dressing mix", "dressing")
        ingredientString = ingredientString.replace("salad dressing", "dressing")
        ingredientString = ingredientString.replace("bourbon whiskey", "bourbon")
        ingredientString = ingredientString.replace("pudding mix", "pudding")

        pluralString = inCheckingPlurals(ingredientString, allIngredients)
        if pluralString:
            ingredientString = pluralString
        else:
            allIngredients.append(ingredientString)

        ingredient["ingredient"] = ingredientString

        #
        # get ingredient labels
        #

        ingredientString = ingredientString.replace("-flavored", "")

        ingredientString = ingredientString.lower()
        splitString = ingredientString.split(" ")
        if '' in splitString:
            splitString.remove('')

        ingredient["labels"] = getLabelsFromArray(splitString)


        if len(ingredient["labels"]) == 0:
            unlabeledIngredients.add(ingredient["ingredient"])

        ingredients.append(ingredient)

    return ingredients


