from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.contrib.auth import authenticate, login
from store.models import Product, ProductReview, Seller, SellerReview, StoreReview
from store.models import Order, Customer

import re
user = authenticate(username='Abhay', password='cmr') ## Use this while debugging.
##user = None ## Use this to force a login.

def calculate_average_rating(reviews): ## TR1 Done.
    """
    Calculate average rating for products and sellers.
    """
    avg_rating = 0.0
    if len(reviews) > 0:
        for review in reviews:
            avg_rating += review.rating
        avg_rating = round(avg_rating / len(reviews), 2)
    return avg_rating

def login_page(request): ## VTR1 Re-do.
    """
    Renders the login page.
    """
    return render(request, 'store/login.html', {})

def login_okay(request): ## TR1 Done.
    """
    Users are redirected to '/' if the login is successful.
    Reload '/shop/login/' if unsuccessful.
    """
    global user
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/shop/')
        else:
            user = None
            return HttpResponseRedirect('/shop/login/')
    else:
        return HttpResponseRedirect('/shop/login/')

def home_page(request): ## VTR1 Done.
    """
    Homepage. Displays all the products available.
    """
    try:
        if user is None:
            return HttpResponseRedirect('/shop/login/')
    except:
        return HttpResponseRedirect('/shop/login/')

    ## Get Products, categories and store reviews.
    all_products_list = Product.objects.all().order_by('product_name')[:10]
    categories = set([product.category for product in all_products_list])
    store_review = StoreReview.objects.all().order_by('time_stamp')[:10]
    context = {'all_products_list':all_products_list, 'categories':categories, 'store_review':store_review, 'user':user}
    return render(request, 'store/home_page.html', context)

def by_search(request): ## VTR1 Done.
    """
    Using the search bar leads you here!
    """
    try:
        if user is None:
            return HttpResponseRedirect('/shop/login/')
    except:
        return HttpResponseRedirect('/shop/login/')
    
    products = Product.objects.all().order_by('product_name')
    name = request.POST['product']
    pattern = ""
    for i in name:
        pattern += '[' + i.lower() + i.upper() + ']'

    ## This name has has been chosen so that I can
    ## reuse the template product_by_category
    all_products_list = []
    for i in products:
        if re.search(pattern, i.product_name) is not None or re.search(pattern, i.seller.seller_name) is not None or re.search(pattern, i.category) is not None:
            all_products_list.append(i)
    
    context = {'all_products_list':all_products_list,
               'product_category':name,
               'from_search':True,
               'user':user}
    return render(request, 'store/by_category.html', context)

def by_category(request, product_category): ## VTR1 Done.
    """
    Displays products by category.
    """
    try:
        if user is None:
            return HttpResponseRedirect('/shop/login/')
    except:
        return HttpResponseRedirect('/shop/login/')

    product_category = product_category[0].upper() + product_category[1:].lower()
    if product_category == 'All':
        all_products_list = Product.objects.all().order_by('product_name')
    else:
        all_products_list = Product.objects.all().filter(category=product_category).order_by('product_name')
    context = {'all_products_list':all_products_list,
               'product_category':product_category,
               'user':user}
    return render(request, 'store/by_category.html', context)

def product(request, product_id): ## VTR2-- Done.
    """
    Displays a particular products' details.
    """
    try:
        if user is None:
            return HttpResponseRedirect('/shop/login/')
    except:
        return HttpResponseRedirect('/shop/login/')

    product = Product.objects.get(pk=product_id)
    seller = Seller.objects.all().filter(seller_name=product.seller)[0] #Wow! :@
    reviews = ProductReview.objects.all().filter(product=product_id)
    avg_rating = calculate_average_rating(reviews)

    ## Related product suggestions.
    related1 = Product.objects.all().filter(seller=product.seller)
    related2 = Product.objects.all().filter(category=product.category)
    related = []
    for Li in related1:
        if Li != product:
            related.append(Li)
    for Li in related2:
        if Li not in related and Li != product:
            related.append(Li)
    import random
    random.shuffle(related)
    del(random)
    ## End of related.

    context = {'product':product, 'seller':seller.pk, 'avg_rating':avg_rating, 'related':related, 'user':user}
    return render(request, 'store/product.html', context)

def product_review(request, product_id): ## VTR1 Done.
    """
    Displays a particular products' reviews.
    """
    try:
        if user is None:
            return HttpResponseRedirect('/shop/login/')
    except:
        return HttpResponseRedirect('/shop/login/')
    
    product = Product.objects.get(pk=product_id)
    reviews = ProductReview.objects.all().filter(product=product_id).order_by('-rating')
    context = {'reviews': reviews, 'product': product.product_name, 'user':user}
    return render(request, 'store/product_review.html', context)

def seller(request, seller_id): ## VTR1 Done.
    """
    Displays a particular sellers' details.
    """
    try:
        if user is None:
            return HttpResponseRedirect('/shop/login/')
    except:
        return HttpResponseRedirect('/shop/login/')
    
    seller = Seller.objects.get(pk=seller_id)
    reviews = SellerReview.objects.all().filter(seller=seller_id)
    avg_rating = calculate_average_rating(reviews)
    context = {'seller': seller, 'avg_rating': avg_rating, 'user':user}
    return render(request, 'store/seller.html', context)

def seller_reviews(request, seller_id): ## VTR1 Done.
    """
    Displays a particular sellers' reviews.
    """
    try:
        if user is None:
            return HttpResponseRedirect('/shop/login/')
    except:
        return HttpResponseRedirect('/shop/login/')
    
    seller = Seller.objects.get(pk=seller_id)
    reviews = SellerReview.objects.all().filter(seller=seller_id).order_by('-rating')
    context = {'reviews': reviews, 'seller': seller.seller_name, 'user':user}
    return render(request, 'store/seller_review.html', context)

def store_reviews(request): ## VTR1 Done.
    """
    Displays all store reviews ordered by time_stamp.
    """
    try:
        if user is None:
            return HttpResponseRedirect('/shop/login/')
    except:
        return HttpResponseRedirect('/shop/login/')
    
    store_reviews = StoreReview.objects.all()
    context = {'store_reviews':store_reviews, 'user':user}
    return render(request, 'store/store_reviews.html', context)

def place_order(request, product_id): ## VTR1 Done.
    """
    Place order and update customer details.
    """
    try:
        if user is None:
            return HttpResponseRedirect('/shop/login/')
    except:
        return HttpResponseRedirect('/shop/login/')
    
    customer = Customer.objects.get(customer_name=user.username)
    product = Product.objects.get(pk=product_id)
    time_of_order = timezone.now()
    ## Decide mode of payment and take appropriate action
    if customer.store_credit >= product.price:
        customer.store_credit -= product.price
        payment_type = 1
    else:
        payment_type = 2
    ## Update purchase history and save instance
    customer.purchase_history += product.price
    customer.save()
    ## Create a new Order object
    order = Order(customer = customer, product = product, status = 1, status_change_time = time_of_order, payment_type = payment_type)
    order.save()

    if payment_type == 1:
        payment_type = 'Paid from store credit'
    else:
        payment_type = 'Cash on delivery'
    context = {'product':product, 'customer':customer, 'time_of_order':time_of_order,
               'payment_type':payment_type, 'user':user}
    return render(request, 'store/order_success.html', context)

def cancel_order(request, order_id): ## TR1 Done.
    try:
        if user is None:
            return HttpResponseRedirect('/shop/login/')
    except:
        return HttpResponseRedirect('/shop/login/')
    try:
        order = Order.objects.get(pk=order_id)
    except:
        return HttpResponse("Invalid order id!")
    if order.status != 5: # 5 = Cancelled, refer models.py
        if order.customer.customer_name == user.username:
            order.status = 5
            order.save()
            return HttpResponseRedirect('/shop/my_orders/')
        return HttpResponse("You do not have permission to cancel this order.")
    return HttpResponse("You have already cancelled this order.")

def my_orders(request): ## VTR1 Done.
    """
    Shows the orders that the particular user has placed.
    """
    try:
        if user is None:
            return HttpResponseRedirect('/shop/login/')
    except:
        return HttpResponseRedirect('/shop/login/')
    
    orders = Order.objects.all().filter(customer__customer_name=user.username).order_by('-status_change_time')
    context = {'user':user, 'orders':orders}
    return render(request, 'store/my_orders.html', context)

def test(request):
    user = authenticate(username='CustomerOne', password='cmr')
    users = [user]
    customer = Customer.objects.all().filter(customer_name=user.username)
    return render(request, 'store/test.html', {'customer':customer,
                                               'users':users})
