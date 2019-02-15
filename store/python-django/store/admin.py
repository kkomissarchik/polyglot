# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Product, Customer, Order, OrderItem

admin.site.register( Product )
admin.site.register( Customer )
admin.site.register( Order )
admin.site.register( OrderItem )
