from django.urls import path
from django.conf.urls import url
from .views import UserProfileDetail, AddUserProfile, UserStatusList, AddUserStatus
from rest_framework.authtoken import views as rest_framework_views
from .views import login_user

urlpatterns = [

    # $$$$$$$$$$$$$$$ User Model $$$$$$$$$$$$$$$
    # For User Authentication
    path('userDetails/', UserProfileDetail.as_view()),
    # To add new User
    path('addUserProfile/', AddUserProfile.as_view()),
    url(r'^get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),
    url(r'^login/$', login_user, name='login'),

    # $$$$$$$$$$$$$$$ User Status Model $$$$$$$$$$$$$$$
    # To add new Status
    path('userStatus/addUserStatus/', AddUserStatus.as_view()),
    # To get user status
    path('userStatus/allUserStatusList/', UserStatusList.as_view()),
]
