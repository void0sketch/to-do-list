"""
URL configuration for AP1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from List import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.todo_list, name='home'),
    path('add/', views.todo_list_create, name='create'),
    path('read/<int:pk>/', views.todo_list_read, name='read'),
    path('update/<int:pk>/', views.todo_list_update, name='update'),
    path('delete/<int:pk>/', views.todo_list_delete, name='delete'),
]
