from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = None
    sort = request.GET.get('sort')
    if sort != None:
        phone = Phone.objects.order_by('-price')
        if 'name' in sort:    
            phone = Phone.objects.order_by('name')
        elif 'min_price' in sort:    
            phone = Phone.objects.order_by('price')
        elif 'max_price' in sort:  
            phone = Phone.objects.order_by('-price')
    else:
        phone = Phone.objects.all()
    return render(request, template, {'phones':phone})


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    return render(request, template, {'phone':phone})
#  

