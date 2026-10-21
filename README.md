# CareerConnect — Django Job & Internship Portal

A beginner-friendly full-stack Django portfolio project for students and recruiters.

## Features
- Student and recruiter registration/login
- Role-based dashboards
- Recruiters can create, edit, and close their own job listings
- Students can search jobs and apply with a resume
- Students can track application status
- Recruiters can review applicants and update application status
- Django Admin
- SQLite database for local development
- Bootstrap responsive templates

## Requirements
- Python 3.11 or 3.12 recommended
- Internet connection for Bootstrap CDN on pages

## Windows setup (PowerShell)
```powershell
cd CareerConnect
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py makemigrations accounts jobs applications
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Open http://127.0.0.1:8000/

If PowerShell blocks activation, use Command Prompt instead:
```bat
.venv\Scripts\activate.bat
```

## First use
1. Register a student account at `/accounts/register/`.
2. Register a recruiter account by selecting Recruiter in the registration form.
3. Recruiter: create a job from the recruiter dashboard.
4. Student: browse jobs and apply with a PDF/DOC/DOCX resume.
5. Admin: visit `/admin/` and sign in with the superuser you created.

## Important notes
- This is a learning/demo project. Before production, configure environment variables, HTTPS, email verification, stronger upload scanning, rate limiting, logging, and production static/media storage.
- Resume uploads are restricted by extension and size in the form, but production applications should also validate file content and use private object storage.
- Do not commit `db.sqlite3`, `.env`, or uploaded resumes to GitHub.
