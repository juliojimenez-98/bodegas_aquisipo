"""bodegas_aquisipo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.urls import include

from bodega_app import views
from productos import views as producto_views

from bodega_app.views import BodegasListView
from productos.views import ProductoListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('home', views.home, name="home"),
    path('home/bodegas', BodegasListView.as_view(), name="bodegas"),
    path("home/bodegas/add", views.add_bodega, name="add-bodega"),
    path("home/productos/add", producto_views.add_producto, name="add_producto"),
    path("home/productos/lista-productos",  ProductoListView.as_view(), name="lista-productos"),


    path("home/bodegas/", include('bodega_app.urls')),
    path("home/productos/", include('productos.urls'))
]
