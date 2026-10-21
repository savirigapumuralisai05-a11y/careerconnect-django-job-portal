from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    full_name = forms.CharField(max_length=120)
    role = forms.ChoiceField(choices=Profile.ROLE_CHOICES)
    class Meta:
        model = User
        fields = ["username", "full_name", "email", "role", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            profile, _ = Profile.objects.get_or_create(user=user)
            profile.full_name = self.cleaned_data["full_name"]
            profile.role = self.cleaned_data["role"]
            profile.save()
        return user
