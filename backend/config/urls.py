"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from music import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('song/list', views.song_list),
    path('song/create', views.song_form_create),
    path('song/<int:pk>/update', views.song_form_update),
    path('song/<int:pk>/get', views.song_form_get),
    path('song/<int:pk>/delete', views.song_delete),

    path('label/list', views.label_list),
    path('label/create', views.label_form_create),
    path('label/<int:pk>/update', views.label_form_update),
    path('label/<int:pk>/get-single-name', views.label_single_name_get),
    path('label/<int:pk>/get', views.label_form_get),
    path('label/<int:pk>/delete', views.label_delete),

    path('musician/list', views.musician_list),
    path('musician/create', views.musician_create),
    path('musician/<int:pk>/update', views.musician_form_update),
    path('musician/<int:pk>/get', views.musician_form_get),
    path('musician/<int:pk>/delete', views.musician_delete),

    url(r'^api-token-auth/', obtain_jwt_token),

]
