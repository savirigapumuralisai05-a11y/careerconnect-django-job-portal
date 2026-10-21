from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ["resume", "cover_letter"]
        widgets = {"cover_letter": forms.Textarea(attrs={"rows": 4, "placeholder": "Tell the recruiter why you fit this role (optional)."})}

    def clean_resume(self):
        resume = self.cleaned_data["resume"]
        if resume.size > 5 * 1024 * 1024:
            raise forms.ValidationError("Resume must be 5 MB or smaller.")
        return resume
