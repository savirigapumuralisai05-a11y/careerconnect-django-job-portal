from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from accounts.models import Profile
from applications.models import Application
from .forms import JobForm
from .models import Job

def home(request):
    query = request.GET.get("q", "").strip()
    job_type = request.GET.get("type", "").strip()
    jobs = Job.objects.filter(is_active=True)
    if query:
        jobs = jobs.filter(Q(title__icontains=query) | Q(company__icontains=query) |
                           Q(location__icontains=query) | Q(description__icontains=query))
    if job_type:
        jobs = jobs.filter(job_type=job_type)
    return render(request, "jobs/home.html", {"jobs": jobs, "query": query, "job_type": job_type})

@login_required
def dashboard(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if profile.role == Profile.RECRUITER:
        jobs = Job.objects.filter(recruiter=request.user)
        return render(request, "jobs/recruiter_dashboard.html", {"jobs": jobs})
    applications = Application.objects.filter(applicant=request.user).select_related("job")
    return render(request, "jobs/student_dashboard.html", {"applications": applications})

def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk, is_active=True)
    already_applied = False
    if request.user.is_authenticated:
        already_applied = Application.objects.filter(job=job, applicant=request.user).exists()
    return render(request, "jobs/job_detail.html", {"job": job, "already_applied": already_applied})

@login_required
def job_create(request):
    if request.user.profile.role != Profile.RECRUITER:
        messages.error(request, "Only recruiter accounts can post jobs.")
        return redirect("dashboard")
    form = JobForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        job = form.save(commit=False)
        job.recruiter = request.user
        job.save()
        messages.success(request, "Job posted successfully.")
        return redirect("dashboard")
    return render(request, "jobs/job_form.html", {"form": form, "heading": "Post a job"})

@login_required
def job_edit(request, pk):
    job = get_object_or_404(Job, pk=pk, recruiter=request.user)
    form = JobForm(request.POST or None, instance=job)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Job updated.")
        return redirect("dashboard")
    return render(request, "jobs/job_form.html", {"form": form, "heading": "Edit job"})

@login_required
def applicants(request, pk):
    job = get_object_or_404(Job, pk=pk, recruiter=request.user)
    rows = Application.objects.filter(job=job).select_related("applicant")
    return render(request, "applications/applicants.html", {"job": job, "applications": rows})
