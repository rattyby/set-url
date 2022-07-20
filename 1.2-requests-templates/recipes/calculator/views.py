from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 300,
        'сыр, г': 50,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def show_recipe(request, dish):
    count = int(request.GET.get('servings', 1))
    recipe = {ingr: amnt * count for ingr, amnt in DATA[dish].items()} if dish in DATA.keys() else {}
    context = {
        'recipe': recipe,
    }
    return render(request, 'calculator/index.html', context)
