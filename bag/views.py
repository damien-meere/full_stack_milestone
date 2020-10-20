from django.shortcuts import render, redirect, reverse, HttpResponse
from products.models import Product
from django.contrib import messages

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    product = Product.objects.get(pk=item_id)
    # gather details from request
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    # session allows browser to store C/S transaction information
    bag = request.session.get('bag', {})

    # if product being added has a size
    if size:
        # if item exists in bag, check if the product is already there
        # if item with the same size, increment.
        # if item has different size, just add to bag
        # else if item isn't already in bag, just add it
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
    else:
        if item_id in list(bag.keys()):
            # if item exists in bag already - increment quantity
            bag[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            # if no item in bag just add item based on quantity provided
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    # overwrite bag dict in session
    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust quantity of the specified product to the shopping bag """
    # gather details from request
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    # session allows browser to store C/S transaction information
    bag = request.session.get('bag', {})

    # if product being adjusted has a size, need to drill down
    # and find specific item with that size
    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
        else:
            # if quantity is zero - delete item
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
    else:
        # for items without a size, just set the bag item
        # quantity to the specified value
        if quantity > 0:
            bag[item_id] = quantity
        else:
            # if quantity is zero - remove item
            bag.pop(item_id)

    # overwrite bag dict in session
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove specified product to the shopping bag """
    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        # session allows browser to store C/S transaction information
        bag = request.session.get('bag', {})

        # if product being adjusted has a size, need to drill down
        # and find specific item with that size and remove it.
        # if items_by_suze dict empty - remove entire item
        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
        else:
            bag.pop(item_id)

        # overwrite bag dict in session
        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
