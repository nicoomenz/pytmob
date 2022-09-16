from django.urls import path
from . import views

urlpatterns = [
     path('<str:key>/', views.redirect_view, name='redirect'),
]
