"""back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.userAuth, name = 'userAuth'),
    path('device/', views.deviceAuth, name = 'deviceAuth'),
    path('beamy/', views.beamyAuth, name = 'beamyAuth'),
    path('device/<int:device_id>/', views.deviceAuthDetail, name = 'deviceAuthDetail'),
    path('beamy/<int:beamy_id>/', views.beamyAuthDetail, name = 'beamyAuthDetail'),
]
