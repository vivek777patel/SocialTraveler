from django.urls import path
from django.conf.urls import url
from .views import AddLocationInfo, LocationInfoDetail, GetLocationInfoDetail, AddVisitedLocationInfo, AddLocationDetails


urlpatterns = [

    # $$$$$$$$$$$$$$$ Location Info Model $$$$$$$$$$$$$$$
    # To add new Status
    path('addLocationInfo/', AddLocationInfo.as_view()),
    # To get user status
    path('allLocationInfoList/', LocationInfoDetail.as_view()),
    path('<int:pk>/', LocationInfoDetail.as_view()),
    path('locationName/<str:location_name>/', GetLocationInfoDetail.as_view(), name="get_location_info"),

    # $$$$$$$$$$$$$$$ Visited Location Model $$$$$$$$$$$$$$$
    path('addVisitedLocationInfo/', AddVisitedLocationInfo.as_view()),

    # $$$$$$$$$$$$$$$ Location Details Model $$$$$$$$$$$$$$$
    path('addLocationDetail/', AddLocationDetails.as_view()),
]
