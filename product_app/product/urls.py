from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path
from product import views

urlpatterns = [
    # path('',views.index,name='index'),
    # path('admin/',admin.site.urls),
    path('',views.home_page),
    path('index/',views.home_page),

    path('prod',views.Add_Product),
    path('prod/', views.Add_Product, name='Add_Product'),
    path('index/index/',views.Add_Product),

    path('show',views.show),
    path('index/show/',views.show),
    path('show/', views.show, name='show'),

    

    # path('delete/<int:id>',views.destroy),
    path('delete1/<int:id>/',views.destroy),
    # path('delete/',views.destroy),
    # path('delete',views.destroy),

    
    
    path('edit/<int:id>',views.edit_product),

    path('update1/<int:id>/', views.update, name='update'),
    # path('update1/<int:id>',views.update),
    path('update1/',views.update),
    
    ]
