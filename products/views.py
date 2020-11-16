from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, ProductReview
from .forms import ProductForm

from checkout.models import Order

from datetime import datetime

# Create your views here.


def all_products(request):
    """ View to return all products """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            # sort used here to preserve original field name
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            # if category is in the GET, split the categories based on
            # the ',' in the url. the filter based on specified category
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any\
                                search parameters")
                return redirect(reverse('products'))

            # Q object allows us to bring an OR operation into the search.
            # This verifies if the search criteria appears in either the name
            # or the descriptions field.
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ Return product and it's reviews and pass to product_detail.html """

    product = get_object_or_404(Product, pk=product_id)
    productReviews = ProductReview.objects.filter(product=product_id)

    context = {
        'product': product,
        'reviews': productReviews,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    # If the user is not a superuser redirect them back to the home
    # page with the message that only store owners can perform this function.
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    # if method is POST, create new instance of form and include
    # request files (images)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        # if valid, save and present a success message
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            # if there was an error, present notification to user
            messages.error(request, 'Failed to add product. Please\
                                     ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product """
    # If the user is not a superuser redirect them back to the home
    # page with the message that only store owners can perform this function.
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    # get product based on the ID thats been passed in,
    # then populate the form with the details of the product
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product Updated!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Product Update Failed. Please\
                                    ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product """
    # If the user is not a superuser redirect them back to the home
    # page with the message that only store owners can perform this function.
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


def edit_product_inventory(product_id, quantity):
    """ Edit a product inventory count"""
    # get product based on the ID thats been passed in,
    # the calculate the new stock count by subtracting the
    # order quantity from the stock_level
    product = get_object_or_404(Product, pk=product_id)
    updated_stock = product.stock_level - quantity
    product.stock_level = updated_stock
    product.save()
    print('Product Updated!')
    return


def product_review(request, order_number):
    # get order
    order = get_object_or_404(Order, order_number=order_number)
    template = 'products/product_review.html'
    context = {
        'order': order,
        'from_profile': True,
    }
    return render(request, template, context)


def add_review(request):
    if request.method == 'POST':
        # Gather Review Elements from Review (PID, Rating & Review text)
        user = request.user
        pid = request.POST.get('pid', '')
        rating = request.POST.get('rating', '')
        review = request.POST.get('review', '')
        # get product instance
        product = get_object_or_404(Product, pk=pid)

        # get Timestamp for review submission in local date and time
        dateTimeObj = datetime.now()
        timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M)")

        # Create and Save Product Review instance
        ProductReview.objects.create(user=str(user),
                                     product=product,
                                     rating=rating,
                                     review=review,
                                     timestamp=timestampStr)

        # We now need to update the product rating based on the review input
        # First get all reviews related to that product
        allReviews = ProductReview.objects.filter(product=pid)
        # Number of Reviews for that product
        reviewtotal = allReviews.count()
        # Get sum of all ratings
        sumRating = 0
        for reviews in allReviews:
            sumRating += reviews.rating

        # Average rating is total Sum / number of reviews
        averageRating = sumRating/reviewtotal
        product.rating = averageRating
        product.save()

        messages.success(request, 'Review Submission Successful!')
        # Return the user to their profile page
        return redirect(reverse('profile'))
