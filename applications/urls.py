from django.urls import path
from . import views

urlpatterns = [
    path("apply/<int:pk>/", views.apply_job, name="apply_job"),
    path("<int:application_id>/status/", views.update_status, name="update_status"),
]
