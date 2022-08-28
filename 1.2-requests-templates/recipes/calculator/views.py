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


def calc_recept(request, bludo):
    context = None
    dictionary = dict()
    servings = request.GET.get('servings', 1)
    if bludo in DATA:
        for key, value in DATA[bludo].items():
            values = value * int(servings)
            dictionary[key] = values

        context = {
            'recipe': dictionary
        }

    return render(request, 'calculator/index.html', context)
