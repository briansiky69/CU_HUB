from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
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
    path('resource_library/', views.resource_library, name='resource_library'),
    path('e-library/', views.document_list, name='document_list'),
    path('logout/', views.logout_view, name='user-logout'),
]