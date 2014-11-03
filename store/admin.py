from django.contrib import admin

from store.models import Seller, SellerReview, Product, ProductReview, StoreReview
from store.models import Customer, Order, Category, SubCategory, Image

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'category_name']

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'category', 'sub_category_name']

class StoreReviewAdmin(admin.ModelAdmin):
    list_display = ['rating', 'review', 'time_stamp', 'sentiment']
    search_fields = ['review']
    list_filter = ['rating']

class SellerReviewAdmin(admin.ModelAdmin):
    list_display = ['seller', 'rating', 'review', 'time_stamp', 'sentiment']
    search_fields = ['seller__seller_name']
    list_filter = ['seller', 'rating']

class SellerAdmin(admin.ModelAdmin):
    search_fields = ['seller']
    list_display = ['seller_name', 'address']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['product', 'customer', 'status', 'status_change_time', 'payment_type']
    search_fields = ['product__seller__seller_name', 'product__product_name']
    list_filter = ['status', 'status_change_time']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'email', 'phone', 'address', 'purchase_history', 'store_credit']
    search_fields = ['customer_name', 'email']

class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'rating', 'review', 'time_stamp', 'sentiment']
    search_fields = ['product']
    list_filter = ['rating']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'price', 'seller', 'category', 'description']
    search_fields = ['product_name', 'seller', 'category']
##    list_filter = ['price']

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(StoreReview, StoreReviewAdmin)
admin.site.register(Seller, SellerAdmin)
admin.site.register(SellerReview, SellerReviewAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Image)
