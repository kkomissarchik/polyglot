# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django import forms
from django.db import transaction
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Customer, CustomerSerializer, Order, Product, ProductSerializer
from .forms import OrderItemFormSet


class HomePageView(TemplateView):
    template_name = "store/home.html"


# Product Views

class ProductListView( ListView ):
    queryset = Product.objects.order_by( "name" )
        

class ProductDetailView( DetailView ):
    model = Product
    

class ProductCreateView( CreateView ):
    model = Product
    fields = [ "name", "price" ]
    
    def get_success_url( self ):
        return reverse( "product", kwargs = { "pk" : self.object.id } )


class ProductUpdateView( UpdateView ):
    model = Product
    fields = [ "name", "price" ]
    
    def get_success_url( self ):
        return reverse( "product", kwargs = { "pk" : self.object.id } )


class ProductDeleteView( DeleteView ):
    model = Product
    success_url = reverse_lazy( "products" )


# Customer Views

class CustomerListView(ListView):
    queryset = Customer.objects.order_by( "-name" )


class CustomerDetailView(DetailView):
    model = Customer


class CustomerCreateView( CreateView ):
    model = Customer
    fields = [ "name", "phone", "address" ]
    
    def get_success_url( self ):
        return reverse( "customer", kwargs = { "pk" : self.object.id } )


class CustomerUpdateView( UpdateView ):
    model = Customer
    fields = [ "name", "phone", "address" ]
    
    def get_success_url( self ):
        return reverse( "customer", kwargs = { "pk" : self.object.id } )


class CustomerDeleteView( DeleteView ):
    model = Customer
    success_url = reverse_lazy( "customers" )


# Order Views

class OrderListView( ListView ):
    queryset = Order.objects.order_by( "id" )


class OrderDetailView( DetailView ):
    model = Order


class OrderCreateView( CreateView ):
    model = Order
    fields = [ "customer", "tax_rate", "shipping", "discount" ]
    
    def get_success_url( self ):
        return reverse( "order", kwargs = { "pk" : self.object.id } )

    def get_context_data( self, **kwargs ):
        data = super( OrderCreateView, self ).get_context_data( **kwargs )
        if self.request.POST:
            data[ 'items' ] = OrderItemFormSet( self.request.POST )
        else:
            data[ 'items' ] = OrderItemFormSet()
        return data

    def form_valid( self, form ):
        context = self.get_context_data()
        items = context[ 'items' ]
        with transaction.atomic():
            self.object = form.save()
            if items.is_valid():
                items.instance = self.object
                items.save()
        return super( OrderCreateView, self ).form_valid( form )


class OrderUpdateView( UpdateView ):
    model = Order
    fields = [ "customer", "tax_rate", "shipping", "discount" ]
    
    def get_success_url( self ):
        return reverse( "order", kwargs = { "pk" : self.object.id } )

    def get_context_data( self, **kwargs ):
        data = super( OrderUpdateView, self ).get_context_data( **kwargs )
        if self.request.POST:
            data[ 'items' ] = OrderItemFormSet( self.request.POST, instance = self.object )
        else:
            data[ 'items' ] = OrderItemFormSet( instance = self.object )
        return data

    def form_valid( self, form ):
        context = self.get_context_data()
        items = context[ 'items' ]
        with transaction.atomic():
            self.object = form.save()
            if items.is_valid():
                items.instance = self.object
                items.save()
        return super( OrderUpdateView, self ).form_valid( form )


class OrderDeleteView( DeleteView ):
    model = Order
    success_url = reverse_lazy( "orders" )


# REST API Views

class ProductApiList( ListCreateAPIView ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductApiDetail( RetrieveUpdateDestroyAPIView ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CustomerApiList( ListCreateAPIView ):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerApiDetail( RetrieveUpdateDestroyAPIView ):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

