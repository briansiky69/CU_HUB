from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from user import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.urls import reverse_lazy


urlpatterns = [
    # path('', views.index, name='homepage'),
    path('', views.homepage, name='homepage'),
    path('edit/', views.edit_event, name='edit'),
    path('contacts/', views.contacts, name='contact'),
    path('events/', views.event_listings, name='events_list'),
    path('give/', views.give, name='give'),
    path('about/', views.about, name='about'),
    path('ministry/', views.ministry, name='ministry'),
    path('ministry/<int:ministry_id>/', views.ministry, name='ministry'),
    path('ministries/', views.ministry_list_view, name='ministries'),
    path('ministry/<int:ministry_id>/', views.ministry_detail_view, name='ministry_detail'),
    # path('ministry/', views.MinistryDetailView, name='MinistryDetailView'),
    path('resource_library/', views.resource_library, name='resource_library'),
    # path('discussion_forums/', views.discussion_forums, name='discussion_forums'),
    # path('group_pages/<int:group_id>/', views.group_pages, name='group_pages'),
    # path('ministry_pages/<int:ministry_id>/', views.ministry_pages, name='ministry_pages'),
    # path('create_event/', views.create_event, name='create_event'),
    # path('edit_event/<int:event_id>/', views.edit_event, name='edit_event'),
    path('register/',views.register,name=('register')),
    path('login', auth_views.LoginView.as_view(
        template_name='user/login.html'), name='user-login'),
    path('profile/', views.userProfile, name='user-profile'),
    path('profile/update/', views.profile_update,
         name='user-profile-update'),
    # path('logout/', auth_views.LogoutView.as_view(
    #     template_name='user/logout.html'), name='user-logout'),
    path('logout/', views.logout_view, name='user-logout'),
]