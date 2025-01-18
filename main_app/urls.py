from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # Team URLs
    path('teams/', views.team_index, name='team-index'),
    path('teams/<int:team_id>/', views.team_detail, name='team-detail'),
    path('teams/create/', views.TeamCreate.as_view(), name='team-create'),
    path('teams/<int:pk>/update/', views.TeamUpdate.as_view(), name='team-update'),
    path('teams/<int:pk>/delete/', views.TeamDelete.as_view(), name='team-delete'),
    # Schedule URLs
    path('schedule/', views.ScheduleList.as_view(), name='schedule-list'),
    path('schedule/create/', views.ScheduleCreate.as_view(), name='schedule-create'),
    path('schedule/<int:pk>/', views.ScheduleDetail.as_view(), name='schedule-detail'),
    path('schedule/<int:pk>/update/', views.ScheduleUpdate.as_view(), name='schedule-update'),
    # Optional: Team-specific schedules
    path('teams/<int:team_id>/schedule/', views.TeamScheduleList.as_view(), name='team-schedule'),
]
