from django.forms import ModelForm, inlineformset_factory

from .models import Order, OrderItem


class OrderItemForm( ModelForm ):
    class Meta:
        model = OrderItem
        exclude = ()


OrderItemFormSet = inlineformset_factory( Order, OrderItem, form = OrderItemForm, extra = 1 )
