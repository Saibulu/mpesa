from django.urls import path

from mpesa.urls import urlpatterns
from . import views


urlpatterns =[
    path('', views.home, name='home'),
    path('stk/', views.stk, name='stk'),
    path('thank_you/', views.thank_you, name='thanks'),
]