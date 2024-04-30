from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_list.as_view(), name='car_list'),
    path('car_create/new/', views.car_create.as_view(), name='car_create'),
    path('update_position/', views.update_position.as_view(), name='update_position'),
    path('update_car/<int:pk>', views.update_car, name='update_car'),
    path('delete_car/<int:pk>/', views.delete_car.as_view(), name='delete_car'),
    path('show_car/<str:color>/', views.show_car.as_view(), name='show_car'),

]