from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect


# Create your views here.
def index(request):
    return render(request, 'index.html')


def product(request, num):
    num = int(num)
    products = ['Рога', 'Копыта', 'Золото']
    imgs = ['img/roga.jpg', 'img/kopita.jpg', 'img/zoloto.jpg']
    data = {'k1': products[num], 'k2': imgs[num]}
    return render(request, 'product.html', context=data)


def contacts(request):
    return render(request, 'contacts.html')


def about(request):
    return render(request, 'about.html')


def month(request, ident):
    ident = int(ident)
    mth = ['Март', 'Апрель', 'Май']
    employers = ['Остап', 'Паниковский', 'Шура']
    imgs = ['img/fe943.jpg', 'img/13187646.jpg', 'img/207535.jpg']
    data = {'k1': mth[ident], 'k2': employers[ident], 'k3': imgs[ident]}
    return render(request, 'month.html', context=data)


def contra(request):
    firms_all = ['Apple', 'Google', 'Yandex', 'Microsoft', 'IBM']
    data = {'firms': firms_all}
    return render(request, 'firms.html', context=data)


def proverka(request, year):
    data = {'year': int(year)}
    return render(request, 'proverka.html', context=data)
