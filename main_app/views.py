from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .models import Team, Schedule, Player

# Team views
class TeamCreate(CreateView):
    model = Team
    fields = ['name', 'city', 'stadium', 'sport', 'logo_url']
    success_url = '/'

class TeamUpdate(UpdateView):
    model = Team
    fields = ['name', 'city', 'stadium', 'sport', 'logo_url']
    success_url = '/'

class TeamDelete(DeleteView):
    model = Team
    success_url = '/'

def home(request):
    teams = Team.objects.all()
    players = Player.objects.all()
    schedules = Schedule.objects.all()
    is_authenticated = request.user.is_authenticated  # Calculate this before the return
    return render(request, 'home.html', {
        'teams': teams,
        'players': players,
        'schedules': schedules,
        'is_authenticated': is_authenticated,  # Add it to the context
    })


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

def schedule_update(request, pk):
    schedule = Schedule.objects.get(id=pk)
    if request.method == "POST":
        home_team_id = request.POST.get('home_team')
        away_team_id = request.POST.get('away_team')
        location = request.POST.get('location')
        game_date = request.POST.get('game_date')
        game_time = request.POST.get('game_time')
        arena = request.POST.get('arena')

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
        'form_errors': []
    })

class ScheduleList(ListView):
    model = Schedule

class ScheduleDetail(DetailView):
    model = Schedule
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        schedule = self.object
        context['home_team_players'] = Player.objects.filter(team=schedule.home_team)
        context['away_team_players'] = Player.objects.filter(team=schedule.away_team)
        return context
    
class ScheduleUpdate(UpdateView):
    model = Schedule
    fields = ['home_team', 'away_team', 'location', 'arena', 'game_date', 'game_time']
    success_url = '/schedule/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teams'] = Team.objects.all()
        return context

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

# Player views
class PlayerCreate(CreateView):
    model = Player
    fields = ['first_name', 'last_name', 'position', 'number', 'team', 'headshot']
    success_url = '/players/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teams'] = Team.objects.all()
        return context
    
class PlayerUpdate(UpdateView):
    model = Player
    fields = ['first_name', 'last_name', 'position', 'number']
    success_url = '/players/'

class PlayerDelete(DeleteView):
    model = Player
    success_url = '/players/'

class PlayerList(ListView):
    model = Player
    success_url = '/players/'

class PlayerDetail(DetailView):
    model = Player
    template_name = 'players/player_detail.html'

# User authentication views
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')