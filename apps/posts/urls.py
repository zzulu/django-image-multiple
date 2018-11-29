from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('new/', views.PostCreate.as_view(), name='create'),
    path('<int:pk>/', views.PostDetail.as_view(), name='detail'),
]
