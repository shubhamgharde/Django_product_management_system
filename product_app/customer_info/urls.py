from django.urls import path
from customer_info.views import *
from django.contrib import admin
from product.urls import *



urlpatterns = [
    
    path('',views.home_page),
    path('index/',views.home_page),

    path('cust/', add_customer),
    path('index/cust/',add_customer),
    path('index/cust/cust/',add_customer),
    path('cust/cust/',add_customer),
    path('cust/cust/cust/',add_customer),
    path('index/cust/cust/cust/',add_customer),

    path('edit/<int:id>',edit_customer),
    
    path('index/cust_list/',show_list_of_custmer),
    path('index/cust_list/',show_list_of_custmer),

   

    path('update/<int:id>', cust_update,),
    path('update/<int:id>/', cust_update,),
    path('update/cust/<int:id>', cust_update,),
    # path('update/', cust_update,),
    path('update/cust/', cust_update,),
    path('update/<int:id>/cust/', cust_update,),

    path('delete/<int:id>/',delete_customer),
    # path('delete/<int:id>',delete_customer),
     

    # path('add_customer/', views.add_customer, name='add_customer'),
    # path('cust_list/', views.cust_list, name='cust_list'),
    # path('cust_update/<int:id>/', views.cust_update, name='cust_update'),

    


]