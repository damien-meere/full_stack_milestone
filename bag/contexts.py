from decimal import Decimal
from django.conf import settings
from products.models import Product
from django.shortcuts import get_object_or_404


def bag_contents(request):
    """ Ensures bag dictionary is available to all templates across site """
    bag_items = []
    total = 0
    product_count = 0
    # get session 'bag', or initialise an empty dict
    bag = request.session.get('bag', {})

    # iterate through items in session 'bag' to get context details
    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            # include product object ot make the objects
            # accessible across all templates
            'product': product,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
