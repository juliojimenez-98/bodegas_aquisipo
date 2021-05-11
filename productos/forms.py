from django import forms

class AddProductoForm(forms.Form):
    nombre_producto = forms.CharField( max_length=500,required=True, widget=forms.TextInput(attrs={'class':'form-control rounded-pill border-0 shadow-sm px-4"', 'placeholder':'Nombre del producto'}))
    descripcion_producto = forms.CharField( max_length=500, required=True,widget=forms.TextInput(attrs={'class':'form-control rounded-pill border-0 shadow-sm px-4"', 'placeholder':'Descripcion del producto'}))