from django.conf import settings
from django.db import models

class Job(models.Model):
    FULL_TIME = "full_time"
    PART_TIME = "part_time"
    INTERNSHIP = "internship"
    JOB_TYPE_CHOICES = [
        (FULL_TIME, "Full-time"), (PART_TIME, "Part-time"), (INTERNSHIP, "Internship")
    ]
    recruiter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posted_jobs")
    title = models.CharField(max_length=160)
    company = models.CharField(max_length=160)
    location = models.CharField(max_length=120)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES, default=INTERNSHIP)
    description = models.TextField()
    requirements = models.TextField(blank=True)
    salary = models.CharField(max_length=100, blank=True, help_text="Optional, e.g. ₹15,000/month")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} at {self.company}"
