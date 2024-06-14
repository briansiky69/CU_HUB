from django.urls import path
from .views import register, login_view, user_logout, profile_update

app_name = 'accounts'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/update/', profile_update, name='profile_update'),
]
