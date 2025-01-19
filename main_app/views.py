from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Team, Schedule

# Team views
class TeamCreate(CreateView):
    model = Team
    fields = ['name', 'city', 'stadium', 'sport', 'logo_url']
    success_url = '/teams/'

class TeamUpdate(UpdateView):
    model = Team
    fields = ['name', 'city', 'stadium', 'sport', 'logo_url']
    success_url = '/teams/'

class TeamDelete(DeleteView):
    model = Team
    success_url = '/teams/'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def team_index(request):
    teams = Team.objects.all()
    return render(request, 'teams/index.html', {'teams': teams})

def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    return render(request, 'teams/detail.html', {'team': team})

# Schedule views
class ScheduleCreate(CreateView):
    model = Schedule
    fields = ['home_team', 'away_team', 'location', 'arena', 'game_date', 'game_time']
    success_url = '/schedule/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teams'] = Team.objects.all()
        return context

    def form_valid(self, form):
        # Print form errors for debugging (if any)
        if form.errors:
            print(form.errors)
        return super().form_valid(form)

def schedule_update(request, pk):
    schedule = Schedule.objects.get(id=pk)

    if request.method == "POST":
        home_team_id = request.POST.get('home_team')
        away_team_id = request.POST.get('away_team')
        location = request.POST.get('location')
        game_date = request.POST.get('game_date')
        game_time = request.POST.get('game_time')
        arena = request.POST.get('arena')

        # Update the existing schedule
        home_team = Team.objects.get(id=home_team_id)
        away_team = Team.objects.get(id=away_team_id)

        schedule.home_team = home_team
        schedule.away_team = away_team
        schedule.location = location
        schedule.game_date = game_date
        schedule.game_time = game_time
        schedule.arena = arena
        schedule.save()

        return redirect('schedule-detail', pk=schedule.id)

    teams = Team.objects.all()
    return render(request, 'schedule_form.html', {
        'teams': teams,
        'schedule': schedule,
        'form_errors': []  # If there are any form errors, they should be passed here
    })

class ScheduleList(ListView):
    model = Schedule

class ScheduleDetail(DetailView):
    model = Schedule

class ScheduleUpdate(UpdateView):
    model = Schedule
    fields = ['home_team', 'away_team', 'location', 'arena', 'game_date', 'game_time']
    success_url = '/schedule/'  # Redirects after the form is successfully updated

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teams'] = Team.objects.all()
        return context

    def form_valid(self, form):
        return super().form_valid(form)

class TeamScheduleList(ListView):
    model = Schedule
    template_name = 'teams/schedule_list.html'
    context_object_name = 'schedule_list'

    def get_queryset(self):
        team_id = self.kwargs['team_id']
        return Schedule.objects.filter(home_team_id=team_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        team = get_object_or_404(Team, id=self.kwargs['team_id'])
        context['team'] = team
        return context