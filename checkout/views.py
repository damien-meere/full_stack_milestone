from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from products.views import edit_product_inventory
from bag.contexts import bag_contents

from profiles.forms import UserProfileForm
from profiles.models import UserProfile

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        # Get Payment intent ID
        pid = request.POST.get('client_secret').split('_secret')[0]
        # setup stripe payment intent and add save info metadata
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})
        # Get the form data from the request
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            # get stripe payment id in order to uniquely id for each
            # transaction so custoemrs can order the same things
            # multiple times and orders will not be confused.
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            # iterate through the bag items to create line items
            for item_id, item_data in bag.items():
                try:
                    # get product ID, if value is int = no size field
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    # if product has size, iterate thoguht eace size and
                    # create line item accordingly
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our \
                            database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    # return user to shopping bag
                    return redirect(reverse('view_bag'))
            # if the user wanted to save their profile redirect to
            # checkout_success with the order number as an additional argument
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your submission. \
                Please re-check your information.')
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There's currently no items in your bag")
            # Reverse Redirect to prevent customers manually accessing URL
            return redirect(reverse('products'))
        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        # prepare stripe payment intent
        stripe_total = round(total*100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        # if user is authenticated, render form with details pre-filled
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            # if user doens't exist, render empty form
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        # if user is not authenticated, render empty form
        else:
            order_form = OrderForm()

    # alert in case the public key has not been set
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    # check if user wanted to save
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    # only save profile details if user is authenticated
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()
        # Once order is complete-  update inventory
        # convert dictionary string to dictionary
        inventory_bag = json.loads(order.original_bag)
        # iterate through bag items
        for item_id, item_data in inventory_bag.items():
            # get product ID, if value is int = no size field
            # product = Product.objects.get(id=item_id)
            # if item_data is an int, product doesnt have a size
            if isinstance(item_data, int):
                edit_product_inventory(item_id, item_data)
            # if product has size, iterate through each size and
            # create line item accordingly
            else:
                for size, quantity in item_data['items_by_size'].items():
                    edit_product_inventory(item_id, quantity)
        # Save the user's info
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            # update the user's profile data
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
