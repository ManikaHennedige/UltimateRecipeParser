#
# checks whether the first argument is the same word as a plural string, checking plurals
#
def equalCheckingPlurals(string, pluralString):
    # only check plurals if first 3 letters match
    if string[0] != pluralString[0]:
        return None

    if len(string) > 1 and len(pluralString) > 1 and string[1] != pluralString[1]:
        return None

    if len(string) > 2 and len(pluralString) > 2 and string[2] != pluralString[2]:
        return None

    # check all possible plurals of string
    if string == pluralString or \
            string + "s" == pluralString or \
            string + "es" == pluralString or \
            string[:-1] + "ies" == pluralString or \
            string[:-1] + "ves" == pluralString:
        return pluralString

    return None


#
# checks whether the first argument matches a string in a list of plurals, checking plurals
#
def inCheckingPlurals(string, pluralList):
    for pluralString in pluralList:
        if equalCheckingPlurals(string, pluralString):
            return pluralString

    return None


# arrays for labeling ingredients (categorized for the purpose of cooking, to tomato is veg, not fruit)
dairyIngredients = ['buttermilk', 'cottage', 'cream', 'creamer', 'creamy', 'creme', 'ghee', 'half-and-half',
                    'milk', 'yogurt']
cheeses = ['bocconcini', 'mozzarella', 'gouda', 'swiss', 'brie']
meats = ['bacon', 'beefs', 'burgers', 'chorizo', 'dogs', 'frankfurters', 'giblets', 'ham', 'lambs', 'livers',
         'meatballs', 'meatloaves', 'meats', 'mignon', 'mincemeat', 'pepperonis', "pig's", 'porks',
         'prosciutto', 'ribs', 'roasts', 'sausages', 'sirloin', 'tripe', 'veal', 'venison', 'kielbasas',
         'liverwurst', 'wieners', 'cotechino', 'linguica', 'pastrami', 'squirrels', 'sauerbraten',
         'picadillo', 'carcass', 'brains', 'mortadella', 'rounds', 'sweetbread', 'toad', 'tinga',
         'embutido', 'hash', 'broil', 'brisket', 'franks', 'pigs', 'rouladen', 'chops', 'scrapple',
         'barbeque', 'spareribs']
poultry = ['bologna', 'bratwursts', 'chickens', 'ducks', 'goose', 'hens', 'pollo', 'salami', 'turkey',
           'pheasant', 'quail', 'turducken', 'drumettes', 'wings', 'roosters']
fish = ['albacores', 'bass', 'catfish', 'cods', 'fish', 'flounder', 'grouper', 'haddock', 'halibut', 'mahi',
        'monkfish', 'salmon', 'shark', 'snapper', 'sole', 'swordfishes', 'trouts', 'tunas', 'bluefish',
        'bonito', 'rockfish', 'mackerel', 'naruto', 'drum', 'marlin', 'tilapia', 'carp', 'kingfish',
        'mullets', 'whitefish', 'kippers', 'torsk', 'saltfish']
seafoods = ['anchovies', 'calamaris', 'clams', 'crabs', 'crabmeat', 'crawfish', 'lobsters', 'mussels',
            'oysters', 'prawns', 'scallops', 'seafood', 'shrimps', 'squids', 'snails', 'shellfish', 'caviar']
mainProteins = ['beans', 'chickpeas', 'nuts', 'seeds', 'tofu', 'whey', 'buckwheat', 'protein', 'soybeans',
                'soy', 'tempeh', 'lentils', 'masoor', 'gluten', 'pine', 'falafel', 'portobello']
fruits = ['apples', 'apricots', 'bananas', 'blackberries', 'blueberries', 'cantaloupe', 'cherries', 'citrons',
          'citrus', 'coconuts', 'cranberries', 'currants', 'elderberries', 'figs', 'fruitcakes', 'fruits',
          'gooseberries', 'grapefruit', 'grapes', 'guava', 'honeydew', 'huckleberries', 'kiwis', 'kumquats',
          'lemonade', 'lemons', 'limes', 'mangoes', 'marrons', 'mincemeat', 'mulberries', 'nectarines', 'oranges',
          'papayas', 'peaches', 'pears', 'persimmon', 'persimmons', 'pineapples', 'plums', 'prunes', 'raisins',
          'raspberries', 'slushies', 'smoothies', 'sorrel', 'strawberries', 'tangerines', 'watermelons', 'yuzu',
          'lingonberries', 'plantains', 'juniper', 'lingonberries', 'pomegranates', 'serviceberries',
          'zinfandel', 'lychees', 'carambola', 'uvas']
vegetables = ['artichokes', 'arugula', 'asparagus', 'avocados', 'bamboo', 'beets', 'broccoli', 'cabbage',
              'calzones', 'carrots', 'cauliflower', 'celery', 'chilis', 'chives', 'choy', 'cilantro', 'coleslaw',
              'coriander', 'cucumber', 'cucumbers', 'dates', 'eggplant', 'eggplants', 'endive', 'escarole',
              'galangal', 'haystacks', 'jicama', 'kale', 'kohlrabi', 'kucai', 'leeks', 'lettuce',
              'mushrooms', 'okra', 'olives', 'onions', 'parsley', 'parsnips', 'peas', 'peppers', 'pickles',
              'pizzas', 'potatoes', 'pumpkins', 'radishes', 'rutabagas', 'salad', 'sauerkraut', 'shallots', 'slaws',
              'spinach', 'sprouts', 'squash', 'tamarind', 'taros', 'tomatillo', 'tomatillos', 'tomatoes', 'turnips',
              'vegetable', 'vegetables', 'veggies', 'watercress', 'yams', 'zucchinis', 'chervil', 'daikon', 'iceberg',
              'nopales', 'pimentos', 'radicchio', 'karengo', 'nori', 'succotash', 'truffle', 'chard', 'fries', 'leaves',
              'browns', 'romain', 'palm', 'sorghum', 'aloo', 'haricots', 'caprese', 'salata', 'shiitake']
sugars = ['Jell-O®', 'butterscotch', 'candied', 'candy', 'caramels', 'frosting', 'fructose', 'gingersnaps',
          'glaces', 'glaze', 'glycerin', 'glycerol', 'gumdrops', 'gummi', 'honey', 'icing', 'jellybeans',
          'ladyfingers', 'licorice', 'macaroons', 'maple', 'marrons glaces', 'marshmallows', 'marzipan',
          'molasses', 'pastries', 'pectin', 'peppermints', 'pie', 'piping', 'puddings', 'puff', 'sourball',
          'sprinkles', 'sucanat', 'sugar', 'sweetener', 'syrup', 'tarts', 'toffee', 'twinkies', 'colaciones'
                                                                                                'sherbet', "hershey®'s",
          'candies', "confectioners'", 'fudge', 'taffy', 'pink', 'sherbet']
sauces = ['alfredo', 'applesauce', 'chutney', 'cannoli', 'dips', 'guacamole', 'hummus', 'paste', 'spreads',
          'tahini', 'tzatziki', 'denjang', 'salsa', 'sauce', 'tapenade', 'coating', 'teriyaki',
          'aioli', 'checca', 'amatriciana', 'ragu', 'marinara']
condiments = ['dressing', 'jam', 'ketchup', 'marinade', 'marjoram', 'mayonnaise', 'mirin', 'mustard',
              'pesto', 'relish', 'shoyu', 'tamari', 'vinaigrette', 'gochujang']
soups = ['broth', 'chowder', 'dashi', 'soup', 'stew', 'jambalaya', 'gumbo', 'gazpacho', 'goulash', 'pho',
         'slumgullion', 'cioppino', 'minestrone']
nuts = ['almonds', 'butternuts', 'candlenuts', 'cashews', 'chestnuts', 'hazelnuts', 'macadamia', 'nuts',
        'peanuts', 'pecans', 'pistachios', 'walnuts', 'nuts']
alcoholicIngredients = ['anisette', 'beer', 'bitters', 'bourbon', 'brandy', 'cacao', 'chambord', 'champagne',
                        'cognac', 'eggnog', 'kirsch', 'kirschwasser', 'liqueur', 'rum', 'schnapps', 'sherry', 'ale',
                        'spritz', 'tequila', 'vermouth', 'vodka', 'whiskey', 'wine', 'campari', 'alcohol', 'absinthe',
                        'cachaca', 'liquor', 'cointreau', 'curacao', 'sake', 'sec', 'calvados', 'galliano', 'lillet',
                        'margaritas', 'coladas', 'negroni', 'mojitos', 'mimosas', 'bahama', 'slammer', 'sauvignon',
                        'chablis',
                        'martinis', 'tequinis', 'spritzs', 'cosmopolitan', 'hurricanes', 'sangria', 'sex', "shaggy's",
                        'nipples',
                        'stoli']
spices = ['allspice', 'anise', 'arrowroot', 'basil', 'bay', 'capers', 'caraway', 'cardamom', 'cassava',
          'cayenne', 'chocolate', 'cilantro', 'cinnamon', 'cloves', 'cocoa', 'coriander', 'cumin', 'dill',
          'fennel', 'flax', 'garlic', 'ginger', 'herbs', 'kalonji', 'mace', 'masala', 'miso', 'monosodium',
          'nutmeg', 'oregano', 'paprika', 'pepper', 'peppercorns', 'pimento', 'poppy', 'poppyseed',
          'powder', 'rhubarb', 'rosemary', 'saffron', 'sage', 'salt', 'savory', 'seasoning', 'sesame', 'spices',
          'sunflower', 'tarragon', 'thyme', 'turmeric', 'vanilla', 'watercress', 'spearmint', 'comfort']
spicy = ['angelica', 'dijon', 'horseradish', 'jerk', 'wasabi', 'spicy']
hotPeppers = ['jalapenos', 'pepperoncinis', 'chiles']
grains = ['bagels', 'baguettes', 'barley', 'biscuits', 'bran', 'bread', 'buns', 'cereal', 'corn', 'cornbread',
          'cornstarch', 'couscous', 'crackers', 'croutons', 'crusts', 'dough', 'granola', 'hominy', 'kasha',
          'masa', 'matzo', 'millet', 'muffins', 'oats', 'pitas', 'popcorn', 'pretzels', 'quinoa', 'rice', 'rolls',
          'shortbread', 'sourdough', 'stuffing', 'tapioca', 'toasts', 'tortillas', 'wheat', 'kaiser', 'cornmeal',
          'breadcrumbs', 'graham', 'bulgur', 'farina', 'oatmeal', 'croissants', 'polenta', 'grits', 'pumpernickel',
          'sago', 'seitan', 'grains', 'taters', 'risotto', 'shells', 'amarettini', 'mochi', 'cornflakes', 'pilaf',
          'puppies']
pastas = ['farfalle', 'fettuccine', 'lasagnas', 'linguine', 'mac', 'macaroni', 'manicotti', 'noodles', 'pasta',
          'farfel', 'vermicelli', 'tagliatelle', 'cannelloni', 'penne']
wrappedMeals = ['burritos', 'calzones', 'dumplings', 'empanadas', 'fajitas', 'hero', 'pie', 'pinwheels', 'pizzas',
                'quesadillas', 'sandwiches', 'tacos', 'tourtiere', 'wontons', 'hoagie', 'pierogies', 'rarebit',
                'joes', 'enchiladas', 'pierogi', 'bierrocks', 'torta', 'reuben', 'wraps', 'piroshki', 'tamales',
                'bruschetta', 'antipasto', 'hamburger', 'muffuletta', 'blanket', 'runzas', 'samosas', 'sambousas',
                'chalupas', 'spanakopita', 'submarine']
pastaDishes = ['casseroles', 'curry', 'lasagna', 'marzetti', 'mostaccioli', 'spaghetti', 'stroganoff', 'ziti',
               'pastini', 'pastitsio', 'fideo', 'spaghettini', 'moussaka', 'tortellinis', 'tallerine', 'talerine',
               'scampi', 'ravioli', 'pad', 'gnocchi', 'spaetzle', 'stromboli']
vegetableDishes = ['tabbouleh', 'kabobs', 'suey', 'frittatas', 'quiches', 'raita', 'shieldzini', 'stir',
                   'sukiyaki']
drinks = ['beverage', 'cider', 'coffee', 'dew™', 'drink', 'eggnog', 'epazote', 'espresso', 'gin', 'juices',
          'lemonade', 'limeade', 'milk', 'rosewater', 'soda', 'tea', 'wassail', 'punch', 'shake', 'shirley',
          'americano']
cookingLiquids = ['oil', 'vinegar', 'water', 'snow', 'ice']
bakingIngredients = ['ammonia', 'baking', 'eggs', 'flour', 'margarine', 'yeast', 'bisquick®']
cookingFats = ['butter', 'gelatin', 'gravy', 'lard', 'lecithin', 'ovalette', 'shortening', 'xanthan', 'suet']
extras = ['carnations', 'coloring', 'dust', 'flowers', 'lilies', 'spray', 'toppings', 'drippings', 'powdered',
          'gold']
fasteners = ['sticks', 'skewers', 'toothpicks']
adhesives = ['glue']
containers = ['jars']
flavorings = ['extract', 'flavorings', 'mint', 'pandan', 'hickory', 'flavored', 'mesquite', 'wood',
              'hardwood']
mixtures = ['food', 'mixes']

# words with succeeding noun ("milk" or "cake")
nonDairyMilks = ['almond', 'soy', 'coconut']
cakeTypes = ['pound', 'sponge', 'white', 'yellow', 'bunny', "'scratch'"]


#
# returns a list of labels that match word(s) in list of ingredient/recipe words
#
def getLabelsFromArray(words):
    labels = set()

    for word in words:
        if inCheckingPlurals(word, dairyIngredients):
            labels.add("dairy")
            labels.add("fat and vitamins")
            continue
        if ("cheese" == word and "cream" not in words) or word in cheeses:
            labels.add("cheese")
            labels.add("dairy")
            continue
        if inCheckingPlurals(word, meats):
            labels.add("meat")
            continue
        if inCheckingPlurals(word, poultry):
            labels.add("poultry")
            continue
        if inCheckingPlurals(word, fish):
            labels.add("fish")
            continue
        if inCheckingPlurals(word, seafoods):
            labels.add("seafood")
            continue
        if inCheckingPlurals(word, mainProteins):
            labels.add("main protein")
            continue
        if inCheckingPlurals(word, fruits):
            labels.add("fruit")
            continue
        if inCheckingPlurals(word, vegetables):
            labels.add("vegetable")
            continue
        if inCheckingPlurals(word, spices):
            labels.add("spice or herb")
            continue
        if inCheckingPlurals(word, sauces):
            labels.add("sauce")
            continue
        if inCheckingPlurals(word, condiments):
            labels.add("condiment")
            continue
        if inCheckingPlurals(word, soups):
            labels.add("soup")
            continue
        if inCheckingPlurals(word, alcoholicIngredients):
            labels.add("alcoholic")
            continue
        if inCheckingPlurals(word, spicy):
            labels.add("spicy")
            continue
        if inCheckingPlurals(word, hotPeppers):
            labels.add("vegetable")
            labels.add("spicy")
            continue
        if inCheckingPlurals(word, nuts):
            labels.add("nut")
            continue
        if inCheckingPlurals(word, cookingLiquids):
            labels.add("cooking liquid")
            continue
        if inCheckingPlurals(word, cookingFats):
            labels.add("cooking fat")
            continue
        if inCheckingPlurals(word, bakingIngredients):
            labels.add("baking ingredient")
            continue
        if inCheckingPlurals(word, sugars):
            labels.add("sugar")
            continue
        if inCheckingPlurals(word, grains):
            labels.add("grain")
            continue
        if inCheckingPlurals(word, pastas):
            labels.add("pasta")
            continue
        if inCheckingPlurals(word, drinks):
            labels.add("drink")
            continue
        if inCheckingPlurals(word, wrappedMeals):
            labels.add("wrapped meal")
            continue
        if inCheckingPlurals(word, pastaDishes):
            labels.add("pasta dish")
            continue
        if inCheckingPlurals(word, vegetableDishes):
            labels.add("vegetable dish")
            continue
        if inCheckingPlurals(word, extras):
            labels.add("recipe extra")
            continue
        if inCheckingPlurals(word, flavorings):
            labels.add("flavoring")
            continue
        if inCheckingPlurals(word, mixtures):
            labels.add("mixture")
            continue
        if inCheckingPlurals(word, fasteners):
            labels.add("fastener")
            continue
        if inCheckingPlurals(word, adhesives):
            labels.add("adhesive")
            continue
        if inCheckingPlurals(word, containers):
            labels.add("container")
            continue

    # check for non dairy milks
    if "milk" in words:
        index = words.index("milk")
        if index > 0 and words[index - 1] in nonDairyMilks:
            labels.remove("dairy")

    # check if "cake" actually is a type of cake
    if "cake" in words:
        index = words.index("cake")
        if index > 0 and words[index - 1] in cakeTypes:
            labels.add("sugar")
    elif "cakes" in words:
        index = words.index("cakes")
        if index > 0 and words[index - 1] in cakeTypes:
            labels.add("sugar")

    # check if "non dairy" in parsed ingredient
    if "dairy" in words and "dairy" in labels:
        index = words.index("dairy")
        if index > 0 and words[index - 1] == "non":
            labels.remove("dairy")

    # add "greens" but not "green" as vegetable
    if "greens" in words:
        labels.add("vegetable")

    # add "steak" as meat only if not used with fish (ie "salmon steak")
    if ("steak" in words or "steaks" in words) and "fish" not in labels:
        labels.add("meat")

    # chili either a pepper or soup
    if "chili" in words:
        index = words.index("chili")

        if index + 1 < len(words) and words[index + 1] == "pepper":
            labels.add("vegetable")
            labels.add("spicy")
        else:
            labels.add("soup")

    # check for unsweetened sugars
    if "unsweetened" in words and "sugar" in labels:
        labels.remove("sugar")

    # check for unflavored flavorings
    if "unflavored" in words and "flavoring" in labels:
        labels.remove("flavoring")

    return list(labels)


# arrays for labeling recipes
breakfasts = ['crepes', 'pancakes', 'waffles', 'eggs', 'beignets', 'doughnuts', 'muffins', 'crepes', 'stroopwaffels',
              'brunch', 'omelets']
desserts = ['cookies', 'cakes', 'brownies', 'pies', 'cobblers', 'mousses', 'puffs', 'biscottis', 'wafers', 'splits',
            'scones', 'cupcakes', 'puddings', 'snowballs', 'candys', 'cheesecakes', 'wafers', 'macaroons', 'fruitcakes',
            'gingerbreads', 'pastries', 'fudges', 'tarts', 'tarte', 'crinkles', 'chews', 'bars', 'squares', 'twists',
            'snaps',
            'brittles', 'thumbprints', 'babka', 'dessert', 'twinkies', 'cannolis', 'genoise', 'stollen', 'panettone',
            'tiramisu', 'tuppakaka', 'vasilopita', 'zeppoli', 'sachertorte', 'spudnuts', 'botercake', 'kolaches',
            'eclairs',
            'ponczki', 'popovers', 'pulla', 'injera', 'dulce', 'bibingka', 'fastnachts', 'springerle', 'spritsar',
            'spruffoli',
            'snickerdoodles', 'santa\'s', 'sandtarts', 'sandbakelser', 'rugelach', 'rocky', 'pralines', 'pfeffernusse',
            'pavlova', 'meringue', 'melting', 'meltaways', 'listy', 'lebkuchen', 'koulourakia', 'hamantashen',
            'fudgies',
            'florentines', 'gods', 'bark', 'buckeyes', 'torte', 'ladyfingers', 'baumkuchen', 'kipferl', 'kake', 'mocha',
            'strufoli', 'stracciatella', 'rosettes', 'pepparkakor', 'sopapillas', 'kolacky', 'kolaczki', 'velvet',
            'yums',
            'vaselopita', 'necklaces', 'tres', 'timbales', 'wandies', 'lizzies', 'kringles', 'meringues', 'gateau',
            'flan',
            'baklava', 'trifle', 'dollies', 'krumkake', 'locks', 'lamingtons', 'napoleons', 'pasties', 'penuche',
            'peppernuts',
            'delights', 'prusurates', 'savoiardi', 'scotcharoos', 'sandies', 'sfinge', 'sfingi', 'rainbows',
            'spitzbuben',
            'sponges', 'spumetti', 'streusel', 'sufganiot', 'sufganiyot', 'crumbcake', 'bliss', 'malasadas']
breads = ['bagels', 'bannock', 'biscuits', 'breads', 'brioche', 'buns', 'challahs', 'chow', 'ciabattas', 'cornbread',
          'crisps', 'croissants', 'doughs', 'focaccia', 'fougassetoast', 'gingerbreads', 'hoska', 'johnnycakes',
          'kaiserbaguettes', 'kiflicrusts', 'kourabiedes', 'lefse', 'loafs', 'loaves', 'naan', 'oatmeal', 'paella',
          'pan', 'paximade', 'pizzelles', 'pumpernickel', 'rolls', 'shells', 'shortbread', 'sourdoughs', 'stuffings',
          'taralli', 'tortillas']


def getRecipeLabels(parsedRecipe):
    labels = set(getLabelsFromArray(parsedRecipe))

    for string in parsedRecipe:
        if inCheckingPlurals(string, breakfasts):
            labels.add("breakfast")
            continue
        if inCheckingPlurals(string, desserts):
            labels.add("dessert")
            continue
        if inCheckingPlurals(string, breads):
            labels.add("bread")
            continue

    # don't use "grain" as "label" if recipe label has "bread"
    if "bread" in labels and "grain" in labels:
        labels.remove("grain")

    if "alcoholic" in labels:
        # if recipe title includes alcohol but no other defining words, it's a drink
        if len(labels) == 1:
            labels.add("drink")

        # if recipe title includes "non-alcoholic", it's not an alcoholic recipe
        if "non-alcoholic" in parsedRecipe:
            labels.remove("alcoholic")

    if "vegetarian" in parsedRecipe:
        if "meat" in labels:
            labels.remove("meat")
        if "seafood" in labels:
            labels.remove("seafood")
        if "fish" in labels:
            labels.remove("fish")
        if "poultry" in labels:
            labels.remove("poultry")

    return list(labels)


# list of measurement units for parsing ingredient
measurementUnits = ['teaspoons', 'tablespoons', 'cups', 'containers', 'packets', 'bags', 'quarts', 'pounds', 'cans',
                    'bottles',
                    'pints', 'packages', 'ounces', 'jars', 'heads', 'gallons', 'drops', 'envelopes', 'bars', 'boxes',
                    'pinches',
                    'dashes', 'bunches', 'recipes', 'layers', 'slices', 'links', 'bulbs', 'stalks', 'squares', 'sprigs',
                    'fillets', 'pieces', 'legs', 'thighs', 'cubes', 'granules', 'strips', 'trays', 'leaves', 'loaves',
                    'halves']


#
# transform amount to cups based on amount and original unit
#
def transformToCups(amount, unit):
    if unit == "cups":
        return amount
    elif unit == "quarts":
        return amount / 16
    elif unit == "quarts":
        return amount / 4
    elif unit == "pints":
        return amount / 2
    elif unit == "ounces":
        return amount * 8
    elif unit == "tablespoons":
        return amount * 16
    elif unit == "teaspoons":
        return amount * 48
    else:
        return amount


# strings indicating ingredient as optional (currently don't use optional boolean for anything)
# optionalStrings = ['optional', 'to taste', 'as needed', 'if desired']

# list of adjectives and participles used to describe ingredients
descriptions = ['baked', 'beaten', 'blanched', 'boiled', 'boiling', 'boned', 'breaded', 'brewed', 'broken', 'chilled',
                'chopped', 'cleaned', 'coarse', 'cold', 'cooked', 'cool', 'cooled', 'cored', 'creamed', 'crisp',
                'crumbled',
                'crushed', 'cubed', 'cut', 'deboned', 'deseeded', 'diced', 'dissolved', 'divided', 'drained', 'dried',
                'dry', 'or more to taste',
                'fine', 'firm', 'fluid', 'fresh', 'frozen', 'grated', 'grilled', 'ground', 'halved', 'hard', 'hardened',
                'heated', 'heavy', 'juiced', 'julienned', 'jumbo', 'large', 'lean', 'light', 'lukewarm', 'marinated',
                'mashed', 'medium', 'melted', 'minced', 'near', 'opened', 'optional', 'packed', 'peeled', 'pitted',
                'popped',
                'pounded', 'prepared', 'pressed', 'pureed', 'quartered', 'refrigerated', 'rinsed', 'ripe', 'roasted',
                'roasted', 'rolled', 'rough', 'scalded', 'scrubbed', 'seasoned', 'seeded', 'segmented', 'separated',
                'shredded', 'sifted', 'skinless', 'sliced', 'slight', 'slivered', 'small', 'soaked', 'soft', 'softened',
                'split', 'squeezed', 'stemmed', 'stewed', 'stiff', 'strained', 'strong', 'thawed', 'thick', 'thin',
                'tied',
                'toasted', 'torn', 'trimmed', 'wrapped', 'vained', 'warm', 'washed', 'weak', 'zested', 'wedged',
                'skinned', 'gutted', 'browned', 'patted', 'raw', 'flaked', 'deveined', 'shelled', 'shucked', 'crumbs',
                'halves', 'squares', 'zest', 'peel', 'uncooked', 'butterflied', 'unwrapped', 'unbaked', 'warmed']

# list of adverbs used before or after description
precedingAdverbs = ['well', 'very', 'super']
succeedingAdverbs = ['diagonally', 'lengthwise', 'overnight']

# list of prepositions used after ingredient name
prepositions = ['as', 'such', 'for', 'with', 'without', 'if', 'about', 'e.g.', 'in', 'into', 'at', 'until']

# only used as <something> removed, <something> reserved, <x> inches, <x> old, <some> temperature
descriptionsWithPredecessor = ['removed', 'discarded', 'reserved', 'included', 'inch', 'inches', 'old', 'temperature',
                               'up']

# descriptions that can be removed from ingredient, i.e. candied pineapple chunks
unnecessaryDescriptions = ['chunks', 'pieces', 'rings', 'spears']

# list of prefixes and suffixes that should be hyphenated
hypenatedPrefixes = ['non', 'reduced', 'semi', 'low']
hypenatedSuffixes = ['coated', 'free', 'flavored']
