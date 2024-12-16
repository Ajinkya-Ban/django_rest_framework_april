from django.contrib import admin
from django.urls import path
from .views import ProdcutListView,ProductCreateView

urlpatterns = [

    path('items/', ProdcutListView.as_view(), name="plist"),
    path('create/',ProductCreateView.as_view(), name="p-create")
]