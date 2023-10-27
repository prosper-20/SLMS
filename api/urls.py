from django.urls import path
from .views import SubjectHomePage, SubjectDetailPage


urlpatterns = [
    path("subject/", SubjectHomePage.as_view(), name="subject-home"),
    path("subject/<slug:slug>/", SubjectDetailPage.as_view(), name="subject-detail")
]