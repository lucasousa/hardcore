from django.urls import path, include
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name="index"),
    path('logout/', views.logout_user, name="logout_user"),
    path('manage_partners/', views.manage_partner, name="manage_partners"),
    path('add_partner/', views.add_partner, name="add_partner"),
    path('views_partner/<int:id>', views.views_partner, name='views_partner'),
    path('manage_products/', views.manage_products, name="manage_products"),
    path('add_product/', views.add_product, name="add_product"),
    path('views_product/<int:id>', views.views_product, name='views_product'),
]
