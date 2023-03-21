from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.utils.html import mark_safe


class ProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput(), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].label = "New Password: "
        self.fields['password'].label_suffix = mark_safe("<br><br>(you cannot view a user's password for security purposes, but you can change it here.)")

    def clean(self):
        super().clean()
        data = self.cleaned_data

        user = User.objects.filter(username=data['username']).exists()
        if user:
            raise ValidationError("A user with this profile already exists.")

    def save(self, commit: bool = ...):
        data = self.cleaned_data
        obj = super().save(commit)

        user = User.objects.create(username=data['username'], email=data['email'])
        user.save()

        if data['password']:
            user.set_password(data['password'])
        obj.user = user

        return obj

    class Meta:
        model = User
        fields = '__all__'
        