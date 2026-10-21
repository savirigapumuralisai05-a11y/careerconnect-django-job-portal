from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from accounts.models import Profile
from jobs.models import Job
from .forms import ApplicationForm
from .models import Application

@login_required
def apply_job(request, pk):
    job = get_object_or_404(Job, pk=pk, is_active=True)
    if request.user.profile.role != Profile.STUDENT:
        messages.error(request, "Only student accounts can apply.")
        return redirect("job_detail", pk=pk)
    if Application.objects.filter(job=job, applicant=request.user).exists():
        messages.info(request, "You have already applied for this job.")
        return redirect("job_detail", pk=pk)
    form = ApplicationForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        application = form.save(commit=False)
        application.job = job
        application.applicant = request.user
        application.save()
        messages.success(request, "Application submitted successfully.")
        return redirect("dashboard")
    return render(request, "applications/apply.html", {"form": form, "job": job})

@login_required
def update_status(request, application_id):
    if request.method != "POST":
        return redirect("dashboard")
    application = get_object_or_404(Application, pk=application_id, job__recruiter=request.user)
    new_status = request.POST.get("status")
    if new_status in dict(Application.STATUS_CHOICES):
        application.status = new_status
        application.save(update_fields=["status"])
        messages.success(request, "Application status updated.")
    return redirect("applicants", pk=application.job_id)
