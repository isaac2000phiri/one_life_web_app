from django.urls import path, include
from django.contrib.auth.decorators import login_required

from .views import *

app_name = 'account'

urlpatterns = [
    path('accounts/signup/', user_signup, name='signup'),
    path('accounts/login/', user_login, name='login'),
    path('', DashboardView.as_view(), name='dashboard'),
    path('users-list/', UserListView.as_view(), name='users-list'),
    path('user_detail/<int:pk>/', UserDetailView.as_view(), name='user-details'),
    
    # path('user_detail/<int:id>/', UserDetailView.as_view(), name='user-detail'),
    
    
]
