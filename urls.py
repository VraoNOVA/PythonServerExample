"""
URL configuration for djangoserver project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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

import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/hello/', views.hello, name='hello'),
    path('api/health/', views.health, name='health'),
    path('api/messages/', views.messages_list, name='messages_list'),
    path('api/messages/<int:message_id>/', views.message_detail, name='message_detail'),
    path('admin/', admin.site.urls),
]
