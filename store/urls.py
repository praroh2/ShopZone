from django.conf.urls import patterns, url

from store import views

urlpatterns = patterns('',
    url(r'^$', views.home_page),
    url(r'^test/$', views.test),
    url(r'^login/$', views.login_page),
    url(r'^login_okay/$', views.login_okay),
    url(r'^my_orders/$', views.my_orders),
    url(r'^store_reviews/$', views.store_reviews),
    url(r'^cancel_order/(?P<order_id>\d+)/$', views.cancel_order),
    url(r'^seller/(?P<seller_id>\d+)/$', views.seller),
    url(r'^seller/(?P<seller_id>\d+)/sellerreviews/$', views.seller_reviews),
    url(r'^(?P<product_id>\d+)/$', views.product),
    url(r'^(?P<product_id>\d+)/productreviews/$', views.product_review),
    url(r'^place_order/(?P<product_id>\d+)/$', views.place_order),
    url(r'^by_search/$', views.by_search),
    url(r'^(?P<product_category>\w+)/$', views.product_by_category),
    )
