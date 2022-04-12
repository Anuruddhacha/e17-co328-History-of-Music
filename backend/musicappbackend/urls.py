"""musicappbackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from musicapp.views import PostView
from musicapp.views import predict
# from django.views import ImageUploadView,GetImagesView 

router = routers.DefaultRouter()
router.register(r'posts', PostView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('upload/', PostView.upload, name='upload'),
    path('predict/', predict, name='predict'),
    path('upload/predict/', predict, name='predict'),
    # path('upload', ImageUploadView.as_view()),
    # path('fetch-images', GetImagesView.as_view()),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
