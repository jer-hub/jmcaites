from django.urls import path

from . import views

app_name='events'
urlpatterns = [
    path('', views.index, name="index"),
    path('add/', views.add, name='add'),
    path('add/process_add', views.process_add, name="process_add")
]