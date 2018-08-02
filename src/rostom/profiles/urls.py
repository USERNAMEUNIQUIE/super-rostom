from django.urls import  path ,include
from . import  views
from rest_framework.routers import  DefaultRouter


router =DefaultRouter()

router.register('hello-viewsest',views.HelloViewSet, base_name='hellow_viewset' )
router.register('profile',views.Userprofileviewsset )
router.register( 'login', views.Loginviewset, base_name= 'login')


urlpatterns = [

    path('hello_view/',views.HelloApiView.as_view()),
    path('',include(router.urls))
]
