"""
URL configuration for contentcanvas project.

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
from base import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('category/<str:cat>/',views.category_articles,name='category'),
    path('articles/<info>',views.single_article,name='single article'),
    path('register/',views.register,name='register page'),
    path('login/',views.login_view,name='login page'),
    path('logout/',views.logout_view,name='logout page'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
