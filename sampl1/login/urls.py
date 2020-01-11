from django.urls import path
from .import views

urlpatterns =[
    path('bis',views.home,name='home'),
    path('add',views.add,name='add')
]