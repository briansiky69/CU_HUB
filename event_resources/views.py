from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import JsonResponse
from django.core.mail import send_mail
import datetime
# from .views import MinistryDetailView
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required





from .models import Event, Resource, Group, Ministry, Membership, Announcement, DiscussionForum, UserProfile, Sermon
from .forms import EventForm


def homepage(request):
    events = Event.objects.all()[:3]
    paginator = Paginator(events, 3) # Show 3 events per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    resources = Resource.objects.all()[:3]
    announcements = Announcement.objects.all()[:3]
    sermons = Sermon.objects.all()[:3]
    # sermons = Sermon.objects.filter(date__gte=datetime.date.today()).order_by('date')

    return render(request, 'homepage.html', {'events': page_obj, 'resources': resources, 'announcements': announcements,'sermons': sermons, })

# def ministry(request,):
#     ministry = [Ministry.objects.get()]
#     events = Event.objects.filter(ministry=ministry)
#     resources = Resource.objects.filter(ministry=ministry)
#     announcements = Announcement.objects.filter(ministry=ministry)
#     return render(request, 'ministry/pages.html', {'ministry': ministry, 'events': events, 'resources': resources, 'announcements': announcements})

# def ministry(request, ):
#     ministry = Ministry.objects.get()
#     events = Event.objects.filter(ministry=ministry)
#     paginator = Paginator(events, 3)  # Show 3 events per page
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     resources = Resource.objects.filter(ministry=ministry)[:3]
#     announcements = Announcement.objects.filter(ministry=ministry)[:3]
#     sermons = Sermon.objects.filter(ministry=ministry)[:3]

#     return render(request, 'ministry/pages.html', {'ministry': ministry, 'events': page_obj, 'resources': resources, 'announcements': announcements, 'sermons': sermons})
def ministry(request):
    ministries = Ministry.objects.all()
    paginator = Paginator(ministries, 3)  # Show 3 ministries per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'ministry/pages.html', {'ministries': page_obj})
# def homepage(request):
#     events = Event.objects.all()
#     paginator = Paginator(events, 3) # Show 3 events per page
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'homepage.html', {'events': page_obj})

# def homepage(request):
#     sermons = Sermon.objects.filter(date__gte=datetime.date.today()).order_by('date')
#     return render(request, 'homepage.html', {'sermons': sermons})

def give(request): 
    return render(request, 'give.html')
def about(request):
    return render(request, 'aboutus.html')
def contacts(request): 
    return render(request, 'contact.html')

def event_listings(request):
    category = request.GET.get('category')
    events = []
    if category:
        events = Event.objects.filter(category=category)
    else:
        events = Event.objects.all()
    paginator = Paginator(events, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'event/listings.html', {'page_obj': page_obj, 'category': category, "events": events})


def ministry_detail_view(request, ministry_id):
    ministry = get_object_or_404(Ministry, id=ministry_id)
    return render(request, 'ministry/ministry_detail.html', {'ministry': ministry})

@login_required(login_url='event_resources:user-login')
def ministry_list_view(request):
    ministries = Ministry.objects.all()
    return render(request, 'ministry/ministry_list.html', {'ministries': ministries})

def ministry_detail_view(request, ministry_slug):
    ministry = get_object_or_404(Ministry, slug=ministry_slug)
    return render(request, 'ministry/ministry_detail.html', {'ministry': ministry})
# class MinistryDetailView(DetailView):
#     model = Ministry
#     template_name = 'ministries/ministry_detail.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         ministry = self.get_object()
#         context['leader_name'] = ministry.leader.get_full_name()
#         return context
# def ministry_detail_view(request, ):
#     ministry = get_object_or_404(Ministry, )
#     view = MinistryDetailView()
#     view.setup(request, )
#     context = view.get_context_data(object=ministry)
#     context['leader_name'] = ministry.leader.get_full_name()
#     return render(request, 'ministry/ministry_detail.html', context)


def resource_library(request):
    category = request.GET.get('category')
    if category:
        resources = Resource.objects.filter(category=category)
    else:
        resources = Resource.objects.all()
    paginator = Paginator(resources, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'resource/library.html', {'page_obj': page_obj, 'category': category})

def discussion_forums(request):
    ministry_id = request.GET.get('ministry')
    if ministry_id:
        discussions = DiscussionForum.objects.filter(ministry_id=ministry_id)
    else:
        discussions = DiscussionForum.objects.all()
    paginator = Paginator(discussions, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app/discussion_forums.html', {'page_obj': page_obj, 'ministry_id': ministry_id})

def group_pages(request, group_id):
    group = Group.objects.get(id=group_id)
    discussions = DiscussionForum.objects.filter(group=group)
    return render(request, 'app/group_pages.html', {'group': group, 'discussions': discussions})


@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.ministry = get_object_or_404(Ministry, id=request.POST['ministry'])
            event.save()
            messages.success(request, 'Event created successfully!')
            return redirect('event_listings')
    else:
        form = EventForm()
    ministries = Ministry.objects.all()
    return render(request, 'app/create_event.html', {'form': form, 'ministries': ministries})

@login_required
def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            event.ministry = get_object_or_404(Ministry, id=request.POST['ministry'])
            event.save()
            messages.success(request, 'Event updated successfully!')
            return redirect('event_listings')
    else:
        form = EventForm(instance=event)
    ministries = Ministry.objects.all()
    return render(request, 'app/edit_event.html', {'form': form, 'event': event, 'ministries': ministries})



def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        # Send an email using the contact information
        send_mail(
            'Contact Form',
            message,
            email,
            ['briansiky69@gmail.com'],
            fail_silently=False,
        )

        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'error'})

# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserRegistrationForm()
#     return render(request, 'user/register.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
           
            return redirect('event_resources:user-login')
    else:
        form = CreateUserForm()
    context = {
        'form': form
    }
    return render(request, 'user/register.html', context)

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('event_resources:homepage')
    else:
        form = UserLoginForm()
    return render(request, 'user/login.html', {'form': form})

def logout_view(request):
    logout(request)
    # Redirect to a specific page after logout
    return render(request, 'user/logout.html')

def userProfile(request):
    context = {

    }
    return render(request, 'user/profile.html', context)

def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('user-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'user/profile_update.html', context)
