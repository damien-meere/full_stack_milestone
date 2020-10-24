from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's currently no items in your bag")
        # Reverse Redirect to prevent customers manually accessing URL
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51H5v9oII1DOczrG4xAuFZE9jU7t1d7fop6wRBE7Yuw6aMx1stP9VSlb7DQpFSLEZTIK9VhxdBafOkegGlOB5NXCZ00QaagRrTW',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
