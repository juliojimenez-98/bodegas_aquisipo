from django.shortcuts import render
from django.shortcuts import redirect
##AUTENTICACION DJANGO
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
##IMPORT MODELS
from bodega_app.models import Bodega

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .forms import AddBodegaForm




#VIEWS


def index(request):
    return render(request, "bodeapp/index.html")

def login_view(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            print("Usuario autenticado", user)
            return redirect('bodegas')
        else:
            messages.error(request, 'Usuario o contraseña no válidos')
            
        
    
    return render(request, "bodeapp/login.html",{

    })

def home(request):

   
    return render(request, "bodeapp/home/home.html")




def logout_view(request):
    logout(request)
    messages.success(request, 'Session cerrada exitosamente')
    return redirect('login')

def add_bodega(request):
    form=AddBodegaForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        numerodebodega = request.POST['nrodebodega']

        descripciondebodega = request.POST['descripcion']

        print(numerodebodega, descripciondebodega)
        bodega = Bodega.objects.create(numero=numerodebodega,descripcion=descripciondebodega)
        if bodega:
            return redirect('bodegas')        

    return render(request, "bodeapp/home/add-bodega.html", {'form':form})



class BodegasListView(ListView):
    template_name = "bodeapp/home/bodegas.html"
    queryset = Bodega.objects.all().order_by('-numero')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = 'Listado de bodegas' 
        context["Bodegas"] = context["object_list"]
        return context
    
class BodegaDetailView(DetailView):
    model = Bodega
    template_name = "bodeapp/home/detalle-bodegas.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context
