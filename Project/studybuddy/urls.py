from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginuser, name="loginuser"),
    path('signup/', views.signupuser, name='signupuser'),

    path('logout/',views.logoutuser, name="logoutuser"),

    path('home/', views.home, name="home"),

    path('room/<str:pk>/', views.room, name="room"),
    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<str:pk>', views.updateRoom, name="update-room"),
    path('delete/<str:pk>', views.deleteRoom, name="delete-room")

]
