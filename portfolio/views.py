from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse


# Create your views here.
class StudentProfileView(View):
    def get(self,request):
        response_data=[{
                "id": 1,
                "name": "Arun Kumar",
                "email": "arun@example.com",
                "phone": "9876543210",
                "location": "Thrissur, Kerala",
                "headline": "Python Full Stack Developer",
                "about": "Aspiring developer interested in building web applications.",
                "profile_image": "https://example.com/arun.jpg"
            }]
        return JsonResponse(response_data,safe=False)

class EducationView(View):
    def get(self,request):
        response_data=[{
                    "id": 1,
                    "institution": "ABC College",
                    "degree": "Bachelor of Computer Applications",
                    "field_of_study": "Computer Applications",
                    "start_year": 2020,
                    "end_year": 2023,
                    "grade": "8.5 CGPA"
                },
                {
                    "id": 2,
                    "institution": "XYZ Higher Secondary School",
                    "degree": "Higher Secondary",
                    "field_of_study": "Computer Science",
                    "start_year": 2018,
                    "end_year": 2020,
                    "grade": "85%"
                }]
        return JsonResponse(response_data,safe=False)

class TechnicalSkillView(View):
    def get(self,request):
        response_data=[
                        {
                            "id": 1,
                            "name": "Python",
                            "category": "Programming Language",
                            "level": "Intermediate"
                        },
                        {
                            "id": 2,
                            "name": "Django REST Framework",
                            "category": "Framework",
                            "level": "Beginner"
                        },
                        {
                            "id": 3,
                            "name": "MySQL",
                            "category": "Database",
                            "level": "Beginner"
                        },
                        {
                            "id": 4,
                            "name": "HTML",
                            "category": "Web Technology",
                            "level": "Intermediate"
                        }
                    ]
        return JsonResponse(response_data,safe=False)

class ProjectsView(View):
    def get(self,request):
        response_data=[
                            {
                                "id": 1,
                                "title": "Smart Expense Tracker",
                                "description": "A web application to manage personal expenses.",
                                "technologies": ["Python", "Django", "MySQL"],
                                "role": "Backend Developer",
                                "github_url": "https://github.com/arun/expense-tracker",
                                "live_url": "https://example.com/expense-tracker"
                            },
                            {
                                "id": 2,
                                "title": "Student Management System",
                                "description": "An application to manage student information.",
                                "technologies": ["Python", "Django", "HTML", "CSS"],
                                "role": "Full Stack Developer",
                                "github_url": "https://github.com/arun/student-management",
                                "live_url":"null"
                            }
                        ]
        return JsonResponse(response_data,safe=False)

class InternshipExperienceView(View):
    def get(self,request):
        response_data= [
                    {
                        "id": 1,
                        "company": "ABC Technologies",
                        "designation": "Python Developer Intern",
                        "location": "Kochi, Kerala",
                        "duration": "3 Months",
                        "description": "Worked on REST API development using Django."
                    }
                ]
        return JsonResponse(response_data,safe=False)

class CertificationsView(View):
    def get(self,request):
        response_data=[
                {
                    "id": 1,
                    "title": "Python Programming",
                    "issuing_organization": "ABC Academy",
                    "year": 2025,
                    "credential_url": "https://example.com/certificate/python"
                },
                {
                    "id": 2,
                    "title": "Web Development",
                    "issuing_organization": "XYZ Institute",
                    "year": 2026,
                    "credential_url": "https://example.com/certificate/web"
                }
            ]
        return JsonResponse(response_data,safe=False)

class AchievmentsView(View):
    def get(self,request):
        response_data=[
                        {
                            "id": 1,
                            "title": "Hackathon Finalist",
                            "organization": "ABC Innovation Challenge",
                            "year": 2025,
                            "description": "Selected as a finalist in a college-level hackathon."
                        },
                        {
                            "id": 2,
                            "title": "College Coding Competition",
                            "organization": "ABC College",
                            "year": 2024,
                            "description": "Secured second position in a coding competition."
                        }
                    ]
        return JsonResponse(response_data,safe=False)

class SocialProfileView(View):
    def get(self,request):
        response_data=[
                    {
                        "platform": "GitHub",
                        "url": "https://github.com/arun"
                    },
                    {
                        "platform": "LinkedIn",
                        "url": "https://linkedin.com/in/arun"
                    },
                    {
                        "platform": "LeetCode",
                        "url": "https://leetcode.com/arun"
                    }
                ]
        return JsonResponse(response_data,safe=False)

class ResumeView(View):
    def get(self,request):
        response_data={
                    "file_name": "Arun_Kumar_Resume.pdf",
                    "resume_url": "https://example.com/resumes/arun-kumar.pdf",
                    "last_updated": "2026-10-20"
                }
        return JsonResponse(response_data,safe=False)
    
                
        



                                            