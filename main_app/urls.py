from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    
    # Authentication URLs
    path('login/', views.login_view, name='login'),  # Use custom login view
    path('logout/', views.logout_view, name='logout'),  # Use custom logout view
    path('signup/', views.signup, name='signup'),  # Custom signup view
    
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
    path('schedule/<int:pk>/update/', views.schedule_update, name='schedule-update'),  
    
    # Optional: Team-specific schedules
    path('teams/<int:team_id>/schedule/', views.TeamScheduleList.as_view(), name='team-schedule'),
    
    # Player URLs
    path('players/', views.PlayerList.as_view(), name='player-list'),
    path('players/create/', views.PlayerCreate.as_view(), name='player-create'),
    path('players/<int:pk>/', views.PlayerDetail.as_view(), name='player-detail'),
    path('players/<int:pk>/update/', views.PlayerUpdate.as_view(), name='player-update'),
    path('players/<int:pk>/delete/', views.PlayerDelete.as_view(), name='player-delete'),  
]
