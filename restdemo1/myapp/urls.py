from django.contrib import admin
from django.urls import path
from .views import ProdcutListView,ProductCreateView,ProductUpdateView,ProdcutDeleteView

urlpatterns = [

    path('items/', ProdcutListView.as_view(), name="plist"),
    path('create/',ProductCreateView.as_view(), name="p-create"),
    path('update-prod/<int:pk>',ProductUpdateView.as_view(),name="update-prod"),
    path('delete-prod/<int:pk>',ProdcutDeleteView.as_view(), name="delete-prod")
]