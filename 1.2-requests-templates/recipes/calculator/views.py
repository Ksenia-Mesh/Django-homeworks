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

def calculator_recipes(requests, dish_get):
    servings = int(requests.GET.get('servings', 1))
    dishes = {}
    for dish, ingredients in DATA.items():
        if dish_get == dish:
            for ing, count in ingredients.items():
                dishes[ing] = count * servings

    context = {
        'recipe': dishes
    }

    return render(requests, 'calculator/index.html', context)

