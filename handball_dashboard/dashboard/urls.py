from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('player/<int:player_id>/', views.player_detail_view, name='player_detail'),
    path('predict/<int:player_id>/', views.predict_performance, name='predict_performance'),
]
