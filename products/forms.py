from django import forms
from .models import Product
from modeltranslation.forms import TranslationModelForm

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'display_name', 'sku')
    