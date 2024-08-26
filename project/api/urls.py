from django.urls import path,include
from rest_framework import routers 
from .views import MovieViewSet
  
# define the router
router = routers.DefaultRouter()
router.register(r'movie', MovieViewSet, basename='movie')

urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls'))
]