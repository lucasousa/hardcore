from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login_user, name="login"),
    path('products_list/', views.product_list, name="product_list"),
    path('partners_list/', views.partner_list, name="partner_list"),
]
