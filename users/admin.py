from users.forms import ProfileForm
from users.models import Comment, Pornstar, Profile
from django.contrib import admin
from django.contrib.auth.models import User


# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'video')


@admin.register(Pornstar)
class PornstarAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    exclude = ('user',)

    form = ProfileForm

    def get_form(self, request, obj = None, **kwargs):
        form = super(ProfileAdmin, self).get_form(request, obj, **kwargs)

        if obj:
            print(obj)
        return form

    def save_model(self, request, obj, form: ProfileForm, change) -> None:
        super().save_model(request, obj, form, change)

    def username(self, profile):
        return profile.user.username

    def email(self, profile):
        return profile.user.email