from django.db import models

# Create your models here.

class StoreReview(models.Model):
    RATING_LEVELS = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        )
    review = models.CharField(max_length=50)
    rating = models.IntegerField(default=3, choices=RATING_LEVELS)
    sentiment = models.IntegerField(default=0)
    time_stamp = models.DateTimeField('Date-time')
    def __str__(self):
        if len(self.review) > 18:
            temp = self.review[:15] + '...'
        else:
            temp = self.review
        return str(self.rating) + ' - ' + temp

class Seller(models.Model):
    seller_name = models.CharField(max_length=15)
    address = models.CharField(max_length=50)
##    payment_due = models.IntegerField(default=0)

    def __str__(self):
        return self.seller_name

class SellerReview(models.Model):
    RATING_LEVELS = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        )
    seller = models.ForeignKey(Seller)
    review = models.CharField(max_length=50)
    rating = models.IntegerField(default=3, choices=RATING_LEVELS)
    sentiment = models.IntegerField(default=0)
    time_stamp = models.DateTimeField('Date-time')
    def __str__(self):
        if len(self.review) > 18:
            temp = self.review[:15] + '...'
        else:
            temp = self.review
        return str(self.seller) + ' - ' + str(self.rating) + ' - ' + temp
    
##class Payment(models.Model):
##    seller = models.ForeignKey(Seller)
##    clearance_time = models.DateTimeField()
##    amount = models.IntegerField(default=0)
##    def __str__(self):
##        return str(self.seller) + ' - ' + str(self.clearance_time)

class Category(models.Model):
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name

class SubCategory(models.Model):
    sub_category_name = models.CharField(max_length=20)
    category = models.ForeignKey(Category)
    
    def __str__(self):
        return self.sub_category_name

class Product(models.Model):
    product_name = models.CharField(max_length=30)
    number_sold = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=50)
    category = models.ForeignKey(SubCategory)
    seller = models.ForeignKey(Seller)
    def __str__(self):
        return self.product_name

class Image(models.Model):
	product = models.ForeignKey(Product)
	link = models.CharField(max_length=2000)
	
	def __str__(self):
		return str(self.product.product_name)

class ProductReview(models.Model):
    RATING_LEVELS = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        )
    product = models.ForeignKey(Product)
    review = models.CharField(max_length=50)
    rating = models.IntegerField(default=3, choices=RATING_LEVELS)
    sentiment = models.IntegerField(default=0)
    time_stamp = models.DateTimeField('Date-time')
    def __str__(self):
        if len(self.review) > 18:
            temp = self.review[:15] + '...'
        else:
            temp = self.review
        return str(self.product) + ' - ' + str(self.rating) + ' - ' + temp

class Customer(models.Model):
    customer_name = models.CharField(max_length=15)
    password = models.CharField(max_length=30, default="cmr")
    address = models.CharField(max_length=50)
    phone = models.IntegerField(default=0)
    email = models.CharField(max_length=20)
    purchase_history = models.IntegerField(default=0)
    store_credit = models.IntegerField(default=0)
    def __str__(self):
        return self.customer_name

class Order(models.Model):
    STATUS_LEVELS = (
        (1, 'New'),
        (2, 'Shipping'),
        (3, 'Delivered'),
        (4, 'Returned'),
        (5, 'Cancelled'),
        )
    PAYMENT_TYPES = (
        (1, 'Paid from store credit'),
        (2, 'Cash on delivery')
    )
    customer = models.ForeignKey(Customer)
    product = models.ForeignKey(Product)
    payment_type = models.IntegerField(choices=PAYMENT_TYPES, default=1)
    status = models.IntegerField(choices=STATUS_LEVELS, default=1)
    status_change_time = models.DateTimeField('Status Change Time')
    def __str__(self):
        return str(self.customer) + ' - ' + str(self.product) + ' - ' + self.get_status_display()
