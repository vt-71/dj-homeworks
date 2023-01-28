from django.shortcuts import render

def recipe (request):
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
    path = request.path
    if 'buter' in path:
         dish = 'buter'
    elif 'omlet' in path:
         dish = 'omlet'
    elif 'pasta' in path:
         dish = 'pasta'
    context = {
    'recipe': DATA [dish]
    }
    servings = 0
    servings = request.GET.get('servings')
    context_1 = context
    if servings != None:
        context_1 = {}
        for context_1 in context.values():
            for k, v in context_1.items():                
                context_1[k] = v * int(servings)
        context_1 = {
        'recipe': context_1
        }
    return render(request, 'index.html', context_1) 

