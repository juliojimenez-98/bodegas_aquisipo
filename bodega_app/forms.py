from django import forms

class AddBodegaForm(forms.Form):
    nrodebodega = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'class':'form-control rounded-pill border border-primary shadow-lg px-4"', 'placeholder':'Numero de bodega'}))
    descripcion = forms.CharField( max_length=500, required=True,widget=forms.TextInput(attrs={'class':'form-control rounded-pill border border-primary shadow-lg px-4"', 'placeholder':'Descripcion de la bodega'}))