from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from .forms import UserRegistrationForm, UserLoginForm, EventForm, ResourceForm, GroupForm, AnnouncementForm, DiscussionForumForm, UserProfileForm
from .models import User, Event, Resource, Group, Ministry, Membership, Announcement, DiscussionForum, UserProfile

def home(request):
    events = Event.objects.all()
    resources = Resource.objects.all()
    return render(request, 'home.html', {'events': events, 'resources': resources})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.ministry = request.user.ministry
            event.save()
            return redirect('home')
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})

@login_required
def create_resource(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES)
        if form.is_valid():
            resource = form.save(commit=False)
            resource.ministry = request.user.ministry
            resource.save()
            return redirect('home')
    else:
        form = ResourceForm()
    return render(request, 'create_resource.html', {'form': form})

@login_required
def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.ministry = request.user.ministry
            group.save()
            return redirect('home')
    else:
        form = GroupForm()
    return render(request, 'create_group.html', {'form': form})

@login_required
def create_announcement(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.ministry = request.user.ministry
            announcement.save()
            return redirect('home')
    else:
        form = AnnouncementForm()
    return render(request, 'create_announcement.html', {'form': form})

@login_required
def create_discussion_forum(request):
    if request.method == 'POST':
        form = DiscussionForumForm(request.POST)
        if form.is_valid():
            discussion_forum = form.save(commit=False)
            discussion_forum.ministry = request.user.ministry
            discussion_forum.user = request.user
            discussion_forum.save()
            return redirect('home')
    else:
        form = DiscussionForumForm()
    return render(request, 'create_discussion_forum.html', {'form': form})

@login_required
def edit(request):
    user = request.user
    if request.method == 'POST':
        user.name = request.POST['name']
        user.email = request.POST['email']
        user.is_student = 'student' in request.POST
        user.is_associate = 'associate' in request.POST
        user.save()
        return redirect('home')
    return render(request, 'edit.html', {'user': user})
