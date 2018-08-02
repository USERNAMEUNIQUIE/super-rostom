from rest_framework.response import Response
from rest_framework import  status
from  .models import Articles
from .serializers import PostSerializer
from django.http import Http404
from rest_framework import  viewsets
from django.shortcuts import get_object_or_404
from django.db.models import Max
from django.http import Http404




class PostList(viewsets.ViewSet):


    def list(self,request):
        Article=Articles.objects.all()

        serializer= PostSerializer(Article ,many=True)
        return Response(serializer.data)

    def create(self,request):
        serializer=PostSerializer(data=request.data)
        if serializer.is_valid():
            newArticle=serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST )

    def retrieve(self, request, pk=None):
        queryset = Articles.objects.all()
        Article = get_object_or_404(queryset, pk=pk)
        serializer = PostSerializer(Article)
        return Response(serializer.data)


    def update(self, request, pk=None):
        queryset = Articles.objects.all()
        Article = get_object_or_404(queryset, pk=pk)
        serializer = PostSerializer(Article,  data=request.data , partial=True)

        serializer.save()
        return Response(serializer.data,{'http_method': 'PATCH'} )

    def destroy(self, request, pk=None):
        queryset = Articles.objects.all()
        Article = get_object_or_404(queryset, pk=pk)

        Article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)












