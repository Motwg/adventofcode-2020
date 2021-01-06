from day21.food import Food


def remove_duplicates(x):
    return list(dict.fromkeys(x))


food = []
its = 8  # 8
with open('input.txt', 'r') as reader:
    for line in reader:
        food.append(Food(line.replace('\n', '')))

dangerous = {}
i = 1
for _ in range(its):
    print('========iteration: ', i)

    allergens, ingredients = [], []
    for f in food:
        for allergen in f.allergens:
            if allergen not in allergens:
                allergens.append(allergen)
        for ingredient in f.ingredients:
            if ingredient not in ingredients:
                ingredients.append(ingredient)
    # print(allergens, ingredients)

    bests = []
    for allergen in allergens:
        d_a = {}
        for f in food:
            f.update(allergen, d_a)
        # print(allergen, d_a)
        x = max(d_a, key=d_a.get)
        bests.append([allergen, x, d_a[x]])
    print(bests)
    s = sorted(bests, key=lambda x: (-x[2], x[0]))
    print(s)
    # xblchx,tr,gzvsg,jlsqx,csqc,fnntr,pmz,lvv
    # xblchx,tr,gzvsg,jlsqx,fnntr,csqc,pmz,lvv
    bests = sorted(bests, key=lambda x: -x[2])
    dangerous[bests[0][0]] = bests[0][1]
    print(bests[0][0], bests[0][1], bests[0][2])
    if i < 7:
        print(bests[1][0], bests[1][1], bests[1][2])
    for f in food:
        f.eliminate(bests[0][0], bests[0][1])
    i += 1

left = 0
for f in food:
    # print(f)
    left += len(f.ingredients)
print(left)
dangerous = dict(sorted(dangerous.items()))
print(','.join(dangerous.values()))
# for k, v in dangerous.items():
#    print(k, v)

# sorted_keys = sorted(dangerous)
# print(dangerous)
# print(sorted_keys)
# vals = []
# for key in sorted_keys:
#     vals.append(dangerous.get(key))
# print(','.join(vals))
