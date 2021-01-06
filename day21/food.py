class Food:

    def __init__(self, entry):
        self.ingredients = entry.split('(')[0].split()
        self.allergens = entry.replace(',', '').replace(')', '').split('contains ')[1].split()

    def __str__(self):
        return str(self.ingredients) + '\n' + str(self.allergens)

    def update(self, allergen, dictionary=None):
        if dictionary is None:
            dictionary = {}
        for key in self.ingredients:
            if allergen in self.allergens:
                if key not in dictionary.keys():
                    dictionary[key] = 1
                else:
                    dictionary[key] += 1

    def eliminate(self, allergen, ingredient):
        if allergen in self.allergens:
            self.allergens.remove(allergen)
        if ingredient in self.ingredients:
            self.ingredients.remove(ingredient)
