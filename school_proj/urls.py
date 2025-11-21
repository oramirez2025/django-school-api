"""
URL configuration for school_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.http import HttpResponse
import math

def rectangle_area_view(request, length, height):
    return HttpResponse(length * height)

def rectangle_perimeter_view(request, length, height):
    return HttpResponse(2 * length + 2 * height)

def circle_area_view(request, radius):
    return HttpResponse(math.pi * radius * radius)

def circle_circumference_view(request, radius):
    return HttpResponse(2 * math.pi * radius)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rectangle/area/length/<int:length>/height/<int:height>/', rectangle_area_view, name='rectangle_area'),
    path('rectangle/perimeter/length/<int:length>/height/<int:height>/', rectangle_perimeter_view, name='rectangle_perimeter'),
    path('circle/area/radius/<int:radius>/', circle_area_view, name='circle_area'),
    path('circle/circumference/radius/<int:radius>/', circle_circumference_view, name='circle_circumference')
]
