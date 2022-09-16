"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from common import views as common_views
from myadmin import views
app_name = 'myadmin'
urlpatterns = [
    path('', views.admin, name="adminpage"),
    path('deletelang/<int:image_id>', views.deletelang, name="deletelang"),
    path('deleteachiv/<int:achiv_id>', views.deleteachiv, name="deleteachiv"),
    path('deletemsg/<int:msg_id>', views.deletemsg, name="deletemsg"),
    path('addlang/', views.addlang, name="addlang"),
    path('addachiv/', views.addachiv, name="addachiv"),
    
]