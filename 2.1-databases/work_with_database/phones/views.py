from django.shortcuts import render, redirect
from phones.models import Phone



def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'

    if request.GET.get('sort') == 'name':
        phone = Phone.objects.all().order_by('name')
    elif request.GET.get('sort') == 'min_price':
        phone = Phone.objects.all().order_by('price')
    elif request.GET.get('sort') == 'max_price':
        phone = Phone.objects.all().order_by('-price')
    else:
        phone = Phone.objects.all()

    context = {
        'phones': phone
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {
        'phone': Phone.objects.get(slug=slug)
    }
    return render(request, template, context)


