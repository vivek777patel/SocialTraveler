from django.urls import path
from django.conf.urls import url
from .views import AddLocationInfo, LocationInfoDetail
from rest_framework.authtoken import views as rest_framework_views

urlpatterns = [

    # $$$$$$$$$$$$$$$ Location Info Model $$$$$$$$$$$$$$$
    # To add new Status
    path('addLocationInfo/', AddLocationInfo.as_view()),
    # To get user status
    path('allLocationInfoList/', LocationInfoDetail.as_view()),
    path('<int:pk>/', LocationInfoDetail.as_view()),
]
