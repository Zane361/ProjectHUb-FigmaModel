from . import views
from django.urls import path

urlpatterns = [
    path('index/', views.HomeListSerializer.as_view()),
    path('portfolio-list/', views.PortfolioListSerializer.as_view()),
    path('team-list/', views.TeamMemberListSerializer.as_view()),
    path('vacancy-list/', views.VacancyListSerializer.as_view()),
    path('vacancy-detail/<str:code>/', views.VacancyDetailSerializer.as_view()),
    path('message-create/', views.message_create),
    path('resume-create/', views.resume_create),
]