# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Cart, CartItem
from gym.models import Product
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'cart/detail.html', {'product': product})


@login_required
def add_to_cart(request, product_id):
    obj, created = Cart.objects.update_or_create(user=request.user)
    obj.save()
    product = Product.objects.get(id=product_id)
    cartItem, createdItem = CartItem.objects.update_or_create(cart= obj, product=product)
    cartItem.save()
    obj.items.add(cartItem)
    return redirect('cart:add_to_cart_detail')


def remove_from_cart(request, product_id):
    obj, created = Cart.objects.update_or_create(user=request.user)
    product = get_object_or_404(Product, id=product_id)
    cartItems = CartItem.objects.filter(cart=obj, product=product)
    cartItems.delete()
    return redirect('cart:add_to_cart_detail')


@login_required
def add_to_cart_detail(request):
    cart = Cart.objects.get(user=request.user)
    # import pdb;pdb.set_trace()
    return render(request, 'cart/cart_detail.html', {'cart': cart})


