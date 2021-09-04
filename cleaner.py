import os
import json

# this segment is to obtain all the file paths for each of the recipe files
recipeDirectory = "D:\\Recipes\\recipes-master\\index"
subDirectories = os.listdir(recipeDirectory)
count = 0
with open("RecipeListPath.txt", "w+") as f:
    for subDirectory in subDirectories:
        recipeFiles = os.listdir(recipeDirectory + "\\" + subDirectory)
        for recipeFile in recipeFiles:
            finalPath = recipeDirectory + "\\" + subDirectory + "\\" + recipeFile + '\n' # newline for display purposes
            # if it's not a json file, we're not interested
            if ".json" not in finalPath:
                continue
            # skip the rest of this chunk if the file is empty - the [:-1] is to get rid of the '\n'
            if os.stat(finalPath[:-1]).st_size == 0:
                continue
            f.write(finalPath)
            count += 1

print("written file path count: ", count)

