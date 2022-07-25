from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sorting = request.GET.get('sort')
    order_string = {'name': 'name', 'min_price': 'price', 'max_price': '-price'}
    if sorting in order_string.keys():
        phone_objects = Phone.objects.all().order_by(order_string[sorting])
    else:
        phone_objects = Phone.objects.all()
    context = {'phones': phone_objects}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_object = Phone.objects.get(slug=slug)
    context = {'phone': phone_object}
    return render(request, template, context)
