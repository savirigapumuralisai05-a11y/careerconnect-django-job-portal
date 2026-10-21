from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/", views.job_detail, name="job_detail"),
    path("create/", views.job_create, name="job_create"),
    path("<int:pk>/edit/", views.job_edit, name="job_edit"),
    path("<int:pk>/applicants/", views.applicants, name="applicants"),
]
