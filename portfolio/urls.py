from django.urls import path
from . import views as portfolio_views, views

urlpatterns = [
    path('home/', portfolio_views.home, name='home'),
    path('about/', views.about, name='about'),
    path('work/', views.work, name='work'), 
    path('contact/', views.contact, name='contact'),
]
