from django.urls import  path
from . import  views


urlpatterns = [

    path('hellow_view/',views.HelloApiView.as_view())
]
