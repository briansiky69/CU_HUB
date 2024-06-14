from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from accounts.models import CustomUser

class Event(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    category = models.CharField(max_length=64)
    ministry = models.ForeignKey('Ministry', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='events/images/', blank=True)
    
class Resource(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    category = models.CharField(max_length=64)
    ministry = models.ForeignKey('Ministry', on_delete=models.CASCADE)
    media = models.FileField()
    is_members_only = models.BooleanField(default=False)

class Group(models.Model):
    name = models.CharField(max_length=128)
    ministry = models.ForeignKey('Ministry', on_delete=models.CASCADE)

class Ministry(models.Model):
    name = models.CharField(max_length=128)
    short_message = models.TextField()
    leader = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ministries/images/', blank=True, null=True)
    leader_email = models.EmailField(blank=True, null=True)
    leader_phone = models.CharField(max_length=32, blank=True, null=True)
    leader_address = models.CharField(max_length=256, blank=True, null=True)

class Membership(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    ministry = models.ForeignKey(Ministry, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

class Announcement(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    ministry = models.ForeignKey('Ministry', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

class DiscussionForum(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    ministry = models.ForeignKey('Ministry', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)



class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state} {self.zip_code}"


class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('male', _('Male')),
        ('female', _('Female')),
    ]
    
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=128, default='',  verbose_name=_('Full Name'))
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, verbose_name=_('Gender'))
    email = models.EmailField(default='', verbose_name=_('Email'))
    phone_regex = RegexValidator(regex=r'^(07|01)\d{8}$', message=_("Phone number must be entered in the format: '07xxxxxx' or '01xxxxxx'."))
    phone = models.CharField(validators=[phone_regex], max_length=10, verbose_name=_('Phone'))
    registration_no = models.CharField(max_length=20, verbose_name=_('Admission No.'))
    course = models.CharField(default='', max_length=128, verbose_name=_('Course'))
    admission_year = models.PositiveIntegerField(default=2020, verbose_name=_('Admission Year'))
    completion_year = models.PositiveIntegerField(default=2024, verbose_name=_('Completion Year'))
    county = models.CharField(default='', max_length=50, verbose_name=_('County'))
    denomination = models.CharField(max_length=50, blank=True, null=True, verbose_name=_('Denomination'))
    e_team = models.CharField(default='',max_length=50, verbose_name=_('E-Team'))
    ministry = models.ForeignKey('Ministry', on_delete=models.SET_NULL, null=True, blank=True, related_name='members')
    comments = models.TextField(blank=True, verbose_name=_('Comments'))
    picture = models.ImageField(upload_to='Userprofile/images/', blank=True, verbose_name=_('Profile Picture'))
    focus_kenya_involvement = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _('User Profile')
        verbose_name_plural = _('User Profiles')

    def __str__(self):
        return self.user.get_full_name()
class Sermon(models.Model):
    title = models.CharField(max_length=128)
    speaker = models.CharField(max_length=128)
    date = models.DateField()
    video_link = models.CharField(blank=True, max_length=255)
    description = models.TextField()
    ministry = models.ForeignKey('Ministry', on_delete=models.CASCADE)
    

    def __str__(self):
        return self.title
    

class ResourceCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Document(models.Model):
    CATEGORY_CHOICES = (
        ('Book', 'Book'),
        ('Magazine', 'Magazine'),
        ('Resource', 'Resource'),
        ('Official Documents', 'Official Documents')
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    document_type = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    file = models.FileField(upload_to='documents/')
    category = models.ForeignKey(ResourceCategory, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, default=None)

    def __str__(self):
        return self.title


class Topic(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='topics')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    topic = models.ForeignKey(
        Topic, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:20]
