from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.ProductListView.as_view(), name='index'),
    
    url(r'^products/?$', views.ProductListView.as_view(), name='products'),
    url(r'^products/(?P<pk>[0-9]+)/?$', views.ProductDetailView.as_view(), name='product'),
    url(r'^products/(?P<pk>[0-9]+)/edit/?$', views.ProductUpdateView.as_view(), name='product-edit'),
    url(r'^products/(?P<pk>[0-9]+)/delete/?$', views.ProductDeleteView.as_view(), name='product-delete'),
    url(r'^products/add/?$', views.ProductCreateView.as_view(), name='product-add'),
    
    url(r'^customers/?$', views.CustomerListView.as_view(), name='customers'),
    url(r'^customers/(?P<pk>[0-9]+)/?$', views.CustomerDetailView.as_view(), name='customer'),
    url(r'^customers/(?P<pk>[0-9]+)/edit/?$', views.CustomerUpdateView.as_view(), name='customer-edit'),
    url(r'^customers/(?P<pk>[0-9]+)/delete/?$', views.CustomerDeleteView.as_view(), name='customer-delete'),
    url(r'^customers/add/?$', views.CustomerCreateView.as_view(), name='customer-add'),

    url(r'^orders/?$', views.OrderListView.as_view(), name='orders'),
    url(r'^orders/(?P<pk>[0-9]+)/?$', views.OrderDetailView.as_view(), name='order'),
    url(r'^orders/(?P<pk>[0-9]+)/edit/?$', views.OrderUpdateView.as_view(), name='order-edit'),
    url(r'^orders/(?P<pk>[0-9]+)/delete/?$', views.OrderDeleteView.as_view(), name='order-delete'),
    url(r'^orders/add/?$', views.OrderCreateView.as_view(), name='order-add'),
    
    url(r'^api/products/?$', views.ProductApiList.as_view()),
    url(r'^api/products/(?P<pk>[0-9]+)/?$', views.ProductApiDetail.as_view()),
    url(r'^api/customers/?$', views.CustomerApiList.as_view()),
    url(r'^api/customers/(?P<pk>[0-9]+)/?$', views.CustomerApiDetail.as_view()),
]
