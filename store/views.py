from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.contrib.auth import authenticate, login
from store.models import Product, ProductReview, Seller, SellerReview, StoreReview
from store.models import Order, Customer, Image

from store import AFINN

import re, random


user = Customer.objects.get(pk=3) ## Use this while debugging.
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

def setiment_analyser(review): ## TR2 Done.
	"""
	Calculates a numerical value to represent the sentiment of a given
	review with the help of AFINN-111.txt.
	"""
	review = review.lower()
	sentiment = 0
	for i in review.split(' '):
		if i in AFINN.vals.keys():
			sentiment += int(AFINN.vals[i])
	return sentiment

def check_match(pattern, i): ## T2 Done.
	"""
	Takes a pattern and a product object. Returns true if the pattern can
	be found in the name, seller, category or sub category.
	"""
	if re.search(pattern, i.product_name) is not None:
		return True
	if re.search(pattern, i.seller.seller_name) is not None:
		return True
	if re.search(pattern, i.category.category.category_name) is not None:
		return True
	if re.search(pattern, i.category.sub_category_name) is not None:
		return True
	return False

def login_page(request): ## VTR1 Re-do.
	"""
	Renders the login page.
	"""
	return render(request, 'store/login.html')

def login_okay(request): ## TR1 Done.
	"""
	Users are redirected to '/' if the login is successful.
	Reload '/shop/login/' if unsuccessful.
	"""
	global user
	username = request.POST['username']
	password = request.POST['password']
	user = None
	try:
		user = Customer.objects.all().filter(customer_name = username)[0]
	except:
		return render(request, "store/login.html", {'errors':["Wrong username or password"]})
		#return HttpResponseRedirect('/shop/login/')
	if user is not None and user.password == password:
		return HttpResponseRedirect('/shop/')
	else:
		return render(request, "store/login.html", {'errors':["Wrong password or password"]})

def signup(request):
	global user
	name = request.POST['name']
	password = request.POST['password']
	repassword = request.POST['repassword']
	address = request.POST['address']
	phone = request.POST['phone']
	email = request.POST['email']

	if password != repassword or password == '':
		return render(request, "store/login.html", {'errors':["Invalid password", "Passwords don't match"]})

	customer = Customer(customer_name = name, password = password, address = address, phone = phone, email = email)
	customer.save()
	user = customer
	return HttpResponseRedirect('/shop/')

def home_page(request): ## VTR1 Done.
	"""
	Homepage. Displays all the products available.
	"""
	print(user)
	try:
		if user is None:
			return HttpResponseRedirect('/shop/login/')
	except:
		return HttpResponseRedirect('/shop/login/')
	## Get Products, categories and store reviews.
	all_products_list = Product.objects.all().order_by('-number_sold')#raw("select * from store_Product order by number_sold")
	categories = set([product.category.category for product in all_products_list])

	store_review = StoreReview.objects.all().order_by('time_stamp')[:10]
	context = {'all_products_list':all_products_list, 'categories':categories, 'store_review':store_review, 'user':user}
	return render(request, 'store/home_page.html', context)

def by_search(request): ## T2 Done.
	"""
	Using the search bar leads you here!
	"""
	try:
		if user is None:
			return HttpResponseRedirect('/shop/login/')
	except:
		return HttpResponseRedirect('/shop/login/')
	name = request.POST['product']
	return HttpResponseRedirect('/shop/by_search/'+name)

def search(request, sub_category): ##T2 done.
	try:
		if user is None:
			return HttpResponseRedirect('/shop/login/')
	except:
		return HttpResponseRedirect('/shop/login/')

	products = Product.objects.all().order_by('product_name')
	pattern = ""
	for i in sub_category:
		pattern += '[' + i.lower() + i.upper() + ']'
	## This name (all_products_list) has has been chosen
	## so that I can reuse the template product_by_category
	## ^^ is no longer applicable, but the name stays!
	all_products_list = []
	for i in products:
		if check_match(pattern, i) == True:
			all_products_list.append(i)
	
	if sub_category == "all":
		all_products_list = Product.objects.all()

	context = {'all_products_list':all_products_list,
			   'product_category':sub_category,
			   'from_search':True,
			   'user':user}
	return render(request, 'store/by_search.html', context)
	
def by_category(request, product_category): ## T2 Done.
	"""
	Displays products by category.
	"""
	try:
		if user is None:
			return HttpResponseRedirect('/shop/login/')
	except:
		return HttpResponseRedirect('/shop/login/')

	product_category = product_category[0].upper() + product_category[1:].lower()
	all_products_list = Product.objects.all()
	sub_categories = list(set([i.category for i in all_products_list if i.category.category.category_name == product_category]))
	context = {'sub_categories': sub_categories, 'product_category': product_category}
	return render(request, 'store/by_category.html', context)

def product(request, product_id): ## T2 Done.
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
	image = Image.objects.all().filter(product=product_id)
	if len(image) > 0:
		image = image[0]

	## Related product suggestions.
	related1 = Product.objects.all().filter(seller=product.seller)
	temp = list(Product.objects.all())
	related2 = []
	for i in temp:
		if i.category.category == product.category.category:
			related2.append(i)
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
	context = {'product':product, 'seller':seller.pk, 'avg_rating':avg_rating, 'related':related, 'image':image, 'user':user}
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
	reviews = ProductReview.objects.all().filter(product=product_id).order_by('-sentiment')
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
	
	customer = Customer.objects.get(customer_name=user.customer_name)
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
		if order.customer.customer_name == user.customer_name:
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
	
	orders = Order.objects.all().filter(customer__customer_name=user.customer_name).order_by('-status_change_time')
	context = {'user':user, 'orders':orders}
	return render(request, 'store/my_orders.html', context)

def my_order_pdf(request, order_id): ## TR2 Done.
	"""
	Generate a PDF of one order.
	"""
	try:
		if user is None:
			return HttpResponseRedirect('/shop/login/')
	except:
		return HttpResponseRedirect('/shop/login/')

	strt1 = 70 ## Table x val's
	strt2 = 250
	order = Order.objects.get(pk = order_id)
	
	from reportlab.pdfgen import canvas
	response = HttpResponse(content_type='application/pdf')
	response['Content_Disposition'] = 'attachment; filename="somefilename.pdf"'

	p = canvas.Canvas(response)
	p.setFont("Helvetica", 35)
	p.setFillColorRGB(0.2, 0.1, 0.3)
	p.drawString(215, 750, "ShopZone")
	p.setFillColorRGB(0.1, 0.2, 0.3)
	p.setFont("Helvetica", 27)
	p.drawString(216, 700, "Order Details")
	p.grid([60, 240, 540], [650, 625, 600, 575, 550, 525, 500, 475])
	p.setFont("Helvetica", 17)
	p.setFillColorRGB(0, 0, 0)
	
	p.drawString(strt1, 630, "Customer Name:")
	p.drawString(strt1, 605, "Order ID:")
	p.drawString(strt1, 580, "Product:")
	p.drawString(strt1, 555, "Price:")
	p.drawString(strt1, 530, "Mode of Payment:")
	p.drawString(strt1, 505, "Status:")
	p.drawString(strt1, 480, "Status Change Time:")

	p.drawString(strt2, 630, str(user.customer_name))
	p.drawString(strt2, 605, str(order.id))
	p.drawString(strt2, 580, str(order.product))
	p.drawString(strt2, 555, str(order.product.price))
	if order.payment_type == 1:
		p.drawString(strt2, 530, "Paid from Store Credit")
	else:
		p.drawString(strt2, 530, "Cash on Delivery")
	if order.status == 1:
		p.drawString(strt2, 505, "New")
	elif order.status == 2:
		p.drawString(strt2, 505, "Shipping")
	elif order.status == 3:
		p.drawString(strt2, 505, "Delivered")
	elif order.status == 4:
		p.drawString(strt2, 505, "Returned")
	elif order.status == 5:
		p.drawString(strt2, 505, "Cancelled")
	p.drawString(strt2, 480, str(order.status_change_time))	
	
	p.showPage()
	p.save()
	return response

def add_product_review(request, product_id):
	rating = int(request.POST['rating'])
	review = request.POST['review']
	if review != "Review":
		sentiment = setiment_analyser(review)
		product_review = ProductReview(product = Product.objects.get(pk=product_id), rating = rating, review = review,
			sentiment = sentiment, time_stamp = timezone.now())
		product_review.save()
		link = '/shop/' + str(product_id) + '/productreviews/'
		return HttpResponseRedirect(link)
	else:
		return HttpResponse("Please type a review")

def add_seller_review(request, seller_id):
	rating = int(request.POST['rating'])
	review = request.POST['review']
	sentiment = setiment_analyser(review)
	seller_review = SellerReview(seller = Seller.objects.get(pk=product_id), rating = rating, review = review,
		sentiment = sentiment, time_stamp = timezone.now())
	seller_review.save()
	link = '/shop/' + str(seller_id) + '/sellerreviews/'
	return HttpResponseRedirect(link)

def test(request):
	all_products_list = Product.objects.all().order_by('-number_sold')
	
	sub_categories = dict()
	for product in all_products_list:
		if product.category.category in sub_categories:
			sub_categories[product.category.category].add(product.category)
		else:
			sub_categories[product.category.category] = set([product.category])
	l = [i.category for i in all_products_list]
	context = {'sub_categories':sub_categories, 'all_products_list': all_products_list, 'l':l}
	return render(request, 'store/test.html', context)
