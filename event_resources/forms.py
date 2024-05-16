from django import forms
from .models import Event, Resource, Ministry
from .models import Event, Resource, Group, Ministry, Membership, Announcement, DiscussionForum, UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = "__all__"

class MinistryForm(forms.ModelForm):
    class Meta:
        model = Ministry
        fields = "__all__"

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = "__all__"

class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = "__all__"

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = "__all__"

class DiscussionForumForm(forms.ModelForm):
    class Meta:
        model = DiscussionForum
        fields = "__all__"

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = "__all__"

class MinistryForm(forms.ModelForm):
    class Meta:
        model = Ministry
        fields = "__all__"


# user platforms
class CreateUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['phone', 'address', 'image']