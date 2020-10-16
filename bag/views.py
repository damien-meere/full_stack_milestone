from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
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
            else:
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(bag.keys()):
            # if item exists in bag already - increment quantity
            bag[item_id] += quantity
        else:
            # if not item in bag just add item base don quantity provided
            bag[item_id] = quantity

    # overwrite bag dict in session
    request.session['bag'] = bag
    return redirect(redirect_url)
