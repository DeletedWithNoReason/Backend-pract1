from django.urls import path
from . import views

urlpatterns = [
    path('', views.hubs_list, name='hubs_list'),
    path('1979_prototype/<int:pk>/', views.hub_detail, name='hub_detail')
]