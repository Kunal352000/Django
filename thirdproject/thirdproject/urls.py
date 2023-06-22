"""
URL configuration for thirdproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# from thirdApp import views
# from thirdApp1 import views     this two line gives error becoz overriding
# from thirdApp.views import greetingInformation
# from thirdApp1.views import timeInformation    this two lines didnt give error but this approach is not good
from thirdApp import views as v1
from thirdApp1 import views as v2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('greeting/',v1.greetingInformation),
    path('time/',v2.timeInformation),
]
