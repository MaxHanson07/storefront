from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Count
from store.models import Product, OrderItem

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

    # Filtering
    # queryset = Product.objects.filter(unit_price__range=(20,30))
    # queryset = Product.objects.filter(title__icontains='coffee')
    # queryset = Product.objects.filter(last_update__date=2021)
    # queryset = Product.objects.filter(description__isnull=True)
    # queryset = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
    # queryset = Product.objects.filter(inventory=F('unit_price'))
    # Sorting
    # queryset = Product.objects.order_by('unit_price', '-title').reverse()
    # queryset = Product.objects.earliest('unit_price')
    # Limiting results
    # queryset = Product.objects.all()[5:10]
    # queryset = Product.objects.values('id', 'title', 'collection__title')
    
    # queryset = Product.objects.filter(
    #     id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')
    
    # (1)
    # queryset = Product.objects.select_related('collection').all()
    # (n)
    # queryset = Product.objects.prefetch_related('promotions').all()

    return render(request, 'hello.html', {'name':'Max'})

    # return HttpResponse('Hello World')