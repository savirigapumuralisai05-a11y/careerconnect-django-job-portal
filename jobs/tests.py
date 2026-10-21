from django.test import TestCase
from django.contrib.auth.models import User
from accounts.models import Profile
from .models import Job

class JobPortalTests(TestCase):
    def test_home_page_loads(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_student_cannot_create_job(self):
        user = User.objects.create_user(username="student1", password="SafePass123!")
        Profile.objects.filter(user=user).update(role=Profile.STUDENT)
        self.client.login(username="student1", password="SafePass123!")
        response = self.client.get("/jobs/create/")
        self.assertEqual(response.status_code, 302)

    def test_job_string_representation(self):
        recruiter = User.objects.create_user(username="recruiter1", password="SafePass123!")
        job = Job.objects.create(recruiter=recruiter, title="Python Intern", company="Demo Co",
                                 location="Remote", description="Learn Django")
        self.assertEqual(str(job), "Python Intern at Demo Co")
