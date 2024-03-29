"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from hello import views

# FIXME: вот тут не вовсем понял как сделать привязку в /hello/urls.py "в файлах urls.py и /hello/urls.py"
urlpatterns = [
    path("", views.index),  # FIXME: тут не соввем понял, главная это "hello/"? "" добавлять было не надо?
    path("hello/", views.index),
    path("hello/about/", views.about),
    path('admin/', admin.site.urls),
]
