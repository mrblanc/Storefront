from django import forms

class AddProduct(forms.Form):
  name = forms.CharField(min_length=3, max_length=50, strip = True)
  description = forms.CharField(max_length=500, strip = True)
  price = forms.DecimalField(min_value=0.00, max_digits=10, decimal_places=2)
