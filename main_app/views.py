from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Team, Schedule

# Team views
class TeamCreate(CreateView):
    model = Team
    fields = '__all__'
    success_url = '/teams/'

class TeamUpdate(UpdateView):
    model = Team
    fields = ["name", "city", "stadium", "sport"]

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
    fields = ['team', 'opponent', 'location', 'arena', 'game_date', 'game_time']
    success_url = '/schedule/'  # Redirects after the form is successfully submitted

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teams'] = Team.objects.all()  # Pass all teams to the template
        return context

    def form_valid(self, form):
        # Print form errors for debugging
        print(form.errors)
        return super().form_valid(form)

class ScheduleList(ListView):
    model = Schedule

class ScheduleDetail(DetailView):
    model = Schedule

class ScheduleUpdate(UpdateView):
    model = Schedule
    fields = ['team', 'opponent', 'location', 'arena', 'game_date', 'game_time']
    success_url = '/schedule/'  # Redirects after the form is successfully updated

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teams'] = Team.objects.all()  # Pass all teams to the template
        return context

    def form_valid(self, form):
        # You can add additional logic here before saving
        return super().form_valid(form)

class TeamScheduleList(ListView):
    model = Schedule
    template_name = 'teams/schedule_list.html'  # Specify a custom template if needed
    context_object_name = 'schedule_list'

    def get_queryset(self):
        team_id = self.kwargs['team_id']
        return Schedule.objects.filter(team_id=team_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        team = get_object_or_404(Team, id=self.kwargs['team_id'])
        context['team'] = team
        return context
