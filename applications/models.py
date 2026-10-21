from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.db import models
from jobs.models import Job

class Application(models.Model):
    PENDING = "pending"
    SHORTLISTED = "shortlisted"
    REJECTED = "rejected"
    STATUS_CHOICES = [
        (PENDING, "Pending"), (SHORTLISTED, "Shortlisted"), (REJECTED, "Rejected")
    ]
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applications")
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="applications")
    resume = models.FileField(upload_to="resumes/", validators=[FileExtensionValidator(["pdf", "doc", "docx"])])
    cover_letter = models.TextField(blank=True, max_length=3000)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        constraints = [
            models.UniqueConstraint(fields=["job", "applicant"], name="one_application_per_job_per_user")
        ]

    def __str__(self):
        return f"{self.applicant.username} → {self.job.title}"
