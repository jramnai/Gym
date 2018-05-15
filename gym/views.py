# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Product
from django.views import generic

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'gym/index.html'
    context_object_name = 'products'
    paginate_by = 12

    def get_queryset(self):
        return Product.objects.all()
