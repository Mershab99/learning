from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('users/', views.userList, name='user-list'),
    path('user/<int:pk>/', views.userDetail, name='user-detail'),
    path('user-create/', views.userCreate, name='user-create'),
    path('user-update/<int:pk>/', views.userUpdate, name='user-update'),
    path('user-delete/<int:pk>/', views.userDelete, name='user-delete'),
]
