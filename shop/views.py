from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact
from math import ceil
from django.contrib import messages
# Create your views here.


def index(request):
    #products = Product.objects.all()
    allProds = []
    catprods = Product.objects.values('category', 'product_Id')
    cats = {item["category"] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds': allProds}
    return render(request, "shop/index.html", params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            contact = Contact(name=name,email=email,phone=phone,subject=subject,message=message)
            contact.save()
            messages.success(request, 'We got your message. We will try to get you')
        except:
            messages.warning(request, 'Submission unsuccessful')
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')


def search(request):
    return render(request, 'shop/search.html')


def productView(request):
    return render(request, 'shop/product.html')


def checkout(request):
    return render(request, 'shop/checkout.html')
