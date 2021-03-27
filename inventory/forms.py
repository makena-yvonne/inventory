from django import forms
from .models import *

class KitchenwareForm(forms.ModelForm):
    class Meta:
        model = Kitchenware
        fields = ('category', 'product', 'quantity', 'status')


class ChickenForm(forms.ModelForm):
    class Meta:
        model = Chicken
        fields = ('category', 'product', 'quantity', 'status')