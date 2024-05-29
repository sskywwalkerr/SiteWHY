from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('shop/', views.shop, name='shop'),
    path('news/', views.news, name='news'),
    path('team/', views.team, name='team'),
    path('categories/', views.categories, name='categories'),
    path('contact/', views.contact, name='contact'),
    path('api-auth/', include('rest_framework.urls')),#new
    #path('ckeditor/', include('ckeditor_uploader.urls')),

    path('auth/', include('djoser.urls')),#new регистрация
    path('auth/', include('djoser.urls.authtoken')),#new сами токены для аккаунтов /auth/token/login
    path('auth/', include('djoser.urls.jwt')),
    path('api/v1/user/',include('blog.user.urls')),
    path("post/", views.PostListView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

