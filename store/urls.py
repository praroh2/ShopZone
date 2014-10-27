from django.conf.urls import patterns, url

from store import views

urlpatterns = patterns('',
    url(r'^$', views.home_page),
    url(r'^test/$', views.test),
    
    url(r'^login/$', views.login_page),
    url(r'^login_okay/$', views.login_okay),
    url(r'^signup/$', views.signup),
    
    url(r'^my_orders/$', views.my_orders),
    url(r'^my_orders/(?P<order_id>\d+)/$', views.my_order_pdf),
    url(r'^cancel_order/(?P<order_id>\d+)/$', views.cancel_order),
    url(r'^place_order/(?P<product_id>\d+)/$', views.place_order),

    
    url(r'^store_reviews/$', views.store_reviews),
    url(r'^seller/(?P<seller_id>\d+)/sellerreviews/$', views.seller_reviews),
    url(r'^(?P<product_id>\d+)/productreviews/$', views.product_review),
    url(r'^(?P<product_id>\d+)/productreviews/add/$', views.add_product_review),
    
    url(r'^seller/(?P<seller_id>\d+)/$', views.seller),
    url(r'^(?P<product_id>\d+)/$', views.product),
    
    url(r'^by_search/$', views.by_search),
    url(r'^by_search/(?P<sub_category>\w+)/$', views.search),
    url(r'^(?P<product_category>\w+)/$', views.by_category),
    )
