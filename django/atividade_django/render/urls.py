from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('verificador/<int:arg_id>', views.verificador, name='outra view')
]
