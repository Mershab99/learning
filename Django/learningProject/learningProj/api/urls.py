from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('users/', views.userList, name='user-list'),
    path('user/<int:pk>/', views.userDetail, name='user-detail'),
    path('user-create/', views.userCreate, name='user-create'),
    path('user-update/<int:pk>/', views.userUpdate, name='user-update'),
    path('user-delete/<int:pk>/', views.userDelete, name='user-delete'),

    path('locations/', views.locationList, name='location-list'),
    path('location/', views.locationDetail, name='location-detail'),
    path('location-create/', views.locationCreate, name='location-create'),
    path('location-update/<int:pk>/', views.locationUpdate, name='location-update'),
    path('location-delete/<int:pk>/', views.locationDelete, name='location-delete'),
    path('user-cards/', views.userCardList, name='user-cards'),
    path('user-card/<int:pk>/', views.userCardDetail, name='user-card'),
    path('user-card-create/', views.userCardCreate, name='user-card-create')


]
