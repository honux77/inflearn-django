from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


from sorl.thumbnail.admin import AdminImageMixin


from .models import Photo
from .models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class PhotoAdmin(AdminImageMixin, admin.ModelAdmin):
    model = Photo


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)


# Register your models here.
admin.site.register(Photo, PhotoAdmin)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


