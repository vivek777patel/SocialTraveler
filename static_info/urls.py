from django.urls import path
from static_info import views

urlpatterns = [
    path('', views.StaticInfoDisp.as_view()),
    path('<int:pk>/', views.StaticInfoDetail.as_view()),
    path('addStaticInfo/', views.AddStatusInfo.as_view()),
    ]