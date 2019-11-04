from django.shortcuts import render, HttpResponse
import stripe
from django.conf import settings


# Create your views here.

def ask_pay(request):
    return render(request, 'payment/ask_payment.html')

def pay_here(request):
    if request.method == 'GET':
        amount = request.GET['amount']
        stripe_public_key = settings.STRIPE_PUBLISHABLE_KEY
        return render(request, 'payment/paying.html', {
            "stripe_public_key": stripe_public_key,
            "amount":int(amount)*100
        })
    else:
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe_token = request.POST["stripeToken"]
        charge = stripe.Charge.create(amount=request.POST["amount"],
            currency='sgd',
            source=stripe_token
        )
        return HttpResponse("Thank you for your donation")