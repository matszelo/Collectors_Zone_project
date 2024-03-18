from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Profile

admin.site.unregister(Group)


class ProfileInUser(admin.StackedInline):
    model = Profile


class ProfileAdmin(admin.ModelAdmin):
    model = User
    fields = ['username', 'password', 'email', 'is_active', 'is_staff', 'is_superuser', ]
    inlines = [ProfileInUser]


admin.site.unregister(User)
admin.site.register(User, ProfileAdmin)
