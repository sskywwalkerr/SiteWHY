from django.shortcuts import render, redirect
from .models import Post
from .serializers import PostSerializer

from rest_framework.response import Response
from rest_framework.views import APIView


def shop(request):
    new = Post.objects.all()
    return render(request, 'shop.html', {'new':new})

def index(request):
    return render(request, 'index.html')
#def shop(request):
    #return render(request, 'shop.html')
def news(request):
    return render(request, 'news.html')
def team(request):
    return render(request, 'team.html')
def categories(request):
    return render(request, 'categories.html')
def contact(request):
    return render(request, 'contact.html')


class PostListView(APIView):
    def get(self,request):
        blog = Post.objects.filter(draft=False)
        serializer = PostSerializer(blog, many=True)
        return Response(serializer.data)