from django.urls import path
from blog.user.views import  UserByToken

urlpatterns = [
    path('user/by/token/', UserByToken.as_view(), name=''),
]