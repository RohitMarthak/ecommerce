from django.http import JsonResponse
from django.shortcuts import render,get_object_or_404
from store.models import Product

from .basket import Basket

def basket_summary(request):
    basket = Basket(request)
    return render(request,'store/basket/summary.html',{'basket':basket})

def basket_add(request):

    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product,id=product_id)
        basket.add(product=product,qty=product_qty)

        basketqty = basket.__len__()
        response = JsonResponse({'qty':basketqty})
        
        return response
    
def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        basket.delete(product=product_id)
        
        subtotal = basket.get_total_price()
        qty = basket.__len__()
        
        response = JsonResponse({'subtotal':subtotal,'qty':qty})
        return response

def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        basket.update(product=product_id, qty=product_qty)

        subtotal = basket.get_total_price()
        qty = basket.__len__()
        totalprice = basket.single_item_price(product_id=product_id)

        response = JsonResponse({'subtotal':subtotal,'qty':qty,'totalprice':totalprice})

        return response

    