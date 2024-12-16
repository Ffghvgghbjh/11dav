# from django.forms import ModelForm
# from .models import Product


# class ProductForm(ModelForm):
#     class Meta:
#         model = Product
#         fields = ['name',
#                   'description',
#                   'price',
#                   'image',
#                   'category']



from django import forms
from django.forms import ModelForm
from .models import Product

class ProductForm(ModelForm):
    SORT_CHOICES = [
        ('name', 'Name'),
        ('price', 'Price'),
        ('category', 'Category'),
    ]
    sort_by = forms.ChoiceField(
        choices=SORT_CHOICES,
        required=False,  
        label="Sort By",
        initial='name',  
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'category']
