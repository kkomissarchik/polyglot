# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return self.name


class ProductSerializer( serializers.ModelSerializer ):

    class Meta:
        model = Product
        fields = ( 'id', 'name', 'price' )


class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.TextField( default = None, blank = True, null = True )
    
    @property
    def json(self):
        return JSONRenderer().render(CustomerSerializer(self).data)

    def __str__(self):
        return self.name


class CustomerSerializer( serializers.ModelSerializer ):

    class Meta:
        model = Customer
        fields = ( 'id', 'name', 'phone', 'address' )


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    @property
    def sub_total(self):
    	return reduce( lambda result, item: result + item.total, self.items.all(), 0 )

    tax_rate = models.DecimalField( max_digits = 4, decimal_places = 2, default = 0, blank = True, null = True, validators = [ MinValueValidator( 0 ) ] )

    @property
    def tax(self):
    	return ( self.sub_total * self.normalize( self.tax_rate ) / 100 ).quantize( Decimal( "0.01" ) )

    shipping = models.DecimalField( max_digits = 8, decimal_places = 2, default = 0, blank = True, null = True, validators = [ MinValueValidator( 0 ) ] )
    discount = models.DecimalField( max_digits = 8, decimal_places = 2, default = 0, blank = True, null = True, validators = [ MinValueValidator( 0 ) ] )
    
    @property
    def total(self):
    	return self.sub_total + self.tax + self.normalize( self.shipping ) - self.normalize( self.discount );
    	
    def normalize(self, number):
        return 0 if number == None else number

    def __str__(self):
        return "Order " + str(self.id) + " for " + self.customer.name


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    @property
    def total(self):
        return self.quantity * self.product.price;

    def __str__(self):
        return str(self.quantity) + " x " + self.product.name + " in " + str(self.order)

