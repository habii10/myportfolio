"""
URL configuration for myportfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from portfolio.views import StudentProfileView
from portfolio.views import EducationView
from portfolio.views import TechnicalSkillView
from portfolio.views import ProjectsView
from portfolio.views import InternshipExperienceView
from portfolio.views import CertificationsView
from portfolio.views import AchievmentsView
from portfolio.views import SocialProfileView
from portfolio.views import ResumeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',StudentProfileView.as_view()),
    path('education/',EducationView.as_view()),
    path('skills/',TechnicalSkillView.as_view()),
    path('projects/',ProjectsView.as_view()),
    path('experience/',InternshipExperienceView.as_view()),
    path('certifications/',CertificationsView.as_view()),
    path('achievments/',AchievmentsView.as_view()),
    path('social-profiles/',SocialProfileView.as_view()),
    path('resumes/',ResumeView.as_view()),
]
