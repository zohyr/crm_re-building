from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('customer/', views.customer, name="c"),
    path('products/', views.product, name="p"),
    path('status/', views.status, name="s")

]