from django.conf import settings
from django.db import models

class Profile(models.Model):
    STUDENT = "student"
    RECRUITER = "recruiter"
    ROLE_CHOICES = [(STUDENT, "Student"), (RECRUITER, "Recruiter")]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=STUDENT)
    full_name = models.CharField(max_length=120, blank=True)
    skills = models.CharField(max_length=300, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} ({self.role})"
