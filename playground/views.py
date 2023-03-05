from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from store.models import Product

# Create your views here.

def say_hello(request):


    # query_set = Product.objects.all()
    # for product in query_set:
    #     print(product)

    # try:
    #     product = Product.objects.get(pk=1)
    # except ObjectDoesNotExist:
    #     pass

    # exists = Product.objects.filter(pk=0).exists()


    # queryset = Product.objects.filter(unit_price__range=(20,30))
    # queryset = Product.objects.filter(title__icontains='coffee')
    # queryset = Product.objects.filter(last_update__date=2021)
    # queryset = Product.objects.filter(description__isnull=True)
    queryset = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))







    return render(request, 'hello.html', {'name':'Max', 'products': list(queryset)})

    # return HttpResponse('Hello World')