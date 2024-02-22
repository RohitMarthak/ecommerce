import stripe
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from basket.basket import Basket

@login_required
def BasketView(request):

    basket = Basket(request)
    total = str(basket.get_total_price())
    total = total.replace('.', '')
    total = int(total)

    stripe.api_key = 'sk_test_51OmO9aSFNo60XOn7FLrkYIh3bVg2dZ4dXSpzqfVKrkqqtpWtM8cM2cBwLEIUOt5ggwPY1n33pfd6CaofIDVrjk4x00fgwfGM5A'
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency='gbp',
        metadata={'userid': request.user.id}
    )

    return render(request, 'payment/home.html', {'client_secret': intent.client_secret})
