
from django.urls import path

from bodega_app import views
from . import views

urlpatterns = [
    
    path("<pk>", views.BodegaDetailView.as_view(), name="detalle-bodega"),
]
