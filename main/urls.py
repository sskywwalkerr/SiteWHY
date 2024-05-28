"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from blog import views
from users import views as userViews
from django.contrib.auth import views as authViews







urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('shop/', views.shop, name='shop'),
    path('news/', views.news, name='news'),
    path('team/', views.team, name='team'),
    path('categories/', views.categories, name='categories'),
    path('contact/', views.contact, name='contact'),
    #path('registration/', userViews.register, name='reg'),
    #path('login/', authViews.LoginView.as_view(template_name='login.html'), name='login'),
    #path('logout/', authViews.LogoutView.as_view(template_name='index.html'), name='logout'),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),#new
    re_path(r'^auth/', include('djoser.urls.authtoken')),#new
    path('api/v1/user/',include('blog.user.urls')),


]

if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

