from django.urls import path
from base.views import product_views as views

urlpatterns=[
    path('',views.getProducts, name='products'),
    path('create/', views.createProduct, name="product-create"),
    path('update/<str:pk>/', views.updateProduct, name="product-update"),
    path('<str:pk>/',views.getProduct, name='product'),
]