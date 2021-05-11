from django.shortcuts import render
from django.shortcuts import redirect

from django.views.generic import ListView

from .models import Producto

from .forms import AddProductoForm

# Create your views here.
class ProductoListView(ListView):
    template_name = "lista-productos.html"
    queryset = Producto.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = 'Listado de productos'
        context["productos"] = context["producto_list"]
        return context
    


def add_producto(request):
    form = AddProductoForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        nombredelproducto = request.POST['nombre_producto']
        descripciondelproducto = request.POST['descripcion_producto']
        

        producto = Producto.objects.create(nombre_producto=nombredelproducto,descripcion_producto=descripciondelproducto)
        print('print')
        if producto:
            return redirect('lista-productos')        

    return render(request, "add-productos.html", {'form':form})

