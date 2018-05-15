from django.conf.urls import url
from . import views

app_name = 'cart'
urlpatterns = [

    # /cart/
    # url(r'^cart/$', views.cart.as_view(), name="cart"),
    url(r'^detail/(?P<product_id>[0-9]+)/$',
        views.detail, name="detail"),
    url(r'^add_to_cart/(?P<product_id>[0-9]+)/$',
        views.add_to_cart, name="add_to_cart"),
    url(r'^remove_from_cart/(?P<product_id>[0-9]+)/$',
        views.remove_from_cart, name="remove_from_cart"),
    url(r'^add_to_cart_detail/$',
        views.add_to_cart_detail, name="add_to_cart_detail"),


]
