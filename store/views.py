from django.shortcuts import get_object_or_404,render
from .models import Category,Product
from django.db.models import Q



def products_all(request):
    products = Product.products.all()
    return render(request,'store/home.html',{'products':products})

def product_detail(request,slug):
    product = get_object_or_404(Product,slug=slug,in_stock=True)
    return render(request,'store/products/single.html',{'product':product})

def category_list(request,category_slug):
    category = get_object_or_404(Category,slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request,'store/products/category.html',{'category':category,'products':products})

def search_list(request):

    q = request.GET.get('q') if request.GET.get('q')!=None else ""

    products = Product.objects.filter(
        Q(slug__icontains=q) |
        Q(category__slug__icontains=q) 
    )
    return render(request,'store/products/search.html',{'products':products})
