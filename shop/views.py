from django.shortcuts import render
from .models import Product
from math import ceil
from django.http import HttpResponse
# Create your views here.
def index(request):
    # products = Product.objects.all()
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))
    allProds = []
    catProds = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catProds}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    # params = {'product': products, 'no_of_slide':nSlides, 'range':range(1,nSlides)}
    # allProds = [[products, range(1, nSlides), nSlides], [products, range(1, nSlides), nSlides]]
    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse("This is contact")

def tracker(request):
    return HttpResponse("This is tracker")

def search(request):
    return HttpResponse("This is search")

def productView(request):
    return HttpResponse("This is prodView")

def checkout(request):
    return HttpResponse("This is checkout")
