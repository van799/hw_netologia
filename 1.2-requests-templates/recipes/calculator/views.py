from os import replace

from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def calc_recept(request, recipe_name):
    context = None
    if recipe_name in DATA:
        data = DATA[recipe_name]
        servings = request.GET.get('servings')

        if servings:
            result = dict()
            for ingredients, quantity in data.items():
                all_ingredients = quantity * int(servings)
                result[ingredients] = all_ingredients
            context = {
                'recipe': result
            }
        else:
            context = {
                'recipe': data
            }
 
    return render(request, 'calculator/index.html', context)
