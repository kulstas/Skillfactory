from django.urls import path
from django.contrib.auth.views import LogoutView

from accounts.views import CustomLoginView, MyAds, get_code, CustomSignUp, ProfileView, ProfileUpdateView


urlpatterns = [
    path('signup', CustomSignUp.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('activation/', get_code, name='activation'),
    path('ads/', MyAds.as_view(), name='ads'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile-update/', ProfileUpdateView.as_view(), name='profile-update'),
]