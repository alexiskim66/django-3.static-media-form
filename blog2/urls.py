from django.contrib import admin
from django.urls import path, include
from blog.views import home
from django.conf import settings
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path('', home2, name='home2'),
    path('<str:id>', detail2, name='detail2'),
    #path('<str:id>', detail, name="recipe_new"),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
