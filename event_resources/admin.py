from django.contrib import admin
from .models import User, Event, Resource, Group, Ministry, Membership, Announcement, DiscussionForum, UserProfile, Sermon, ResourceCategory, Document

admin.site.site_header = 'CU HUB Adminstrtor'
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_student', 'is_associate')
    search_fields = ('name', 'email')

# admin.site.register(User, UserAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'start_time', 'end_time', 'category', 'ministry')
    search_fields = ('name', 'description')

admin.site.register(Event, EventAdmin)

class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'category', 'ministry', 'media', 'is_members_only')
    search_fields = ('title', 'description')

admin.site.register(Resource, ResourceAdmin)

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'ministry')
    search_fields = ('name',)

admin.site.register(Group, GroupAdmin)

class MinistryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Ministry, MinistryAdmin)

class MembershipAdmin(admin.ModelAdmin):
    list_display = ('user', 'ministry', 'date_joined', 'invite_reason')
    search_fields = ('user__name', 'ministry__name')

admin.site.register(Membership, MembershipAdmin)

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'ministry', 'created_on')
    search_fields = ('title', 'content')

admin.site.register(Announcement, AnnouncementAdmin)

class DiscussionForumAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'ministry', 'created_on', 'user')
    search_fields = ('title', 'content')

admin.site.register(DiscussionForum, DiscussionForumAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'picture')
    search_fields = ('user__name',)

admin.site.register(UserProfile, UserProfileAdmin)

admin.site.register(Sermon)
admin.site.register(ResourceCategory)
admin.site.register(Document)
