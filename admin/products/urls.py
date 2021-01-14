from django.urls import path
from .views import ProductViewSets, UserAPIView

urlpatterns = [
    path('products', ProductViewSets.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('products/<str:pk>', ProductViewSets.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('user', UserAPIView.as_view()),

]
