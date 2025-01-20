from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Team Model
class Team(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    stadium = models.CharField(max_length=255)
    sport = models.CharField(max_length=255)
    logo_url = models.URLField(max_length=500, blank=True, null=True)
    manager = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='managed_team')

    def __str__(self):
        return f"{self.name} - {self.city} - {self.stadium} - {self.sport}"
    
    def get_absolute_url(self):
        return reverse('team-detail', kwargs={'team_id': self.id})


# Player Model
class Player(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    number = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position} - #{self.number}"
    
    def get_absolute_url(self):
        return reverse('player-detail', kwargs={'player_id': self.id})

# Schedule Model
class Schedule(models.Model):
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_games')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_games')
    location = models.CharField(max_length=255)
    game_date = models.DateField()
    game_time = models.TimeField()
    arena = models.TextField()

    def __str__(self):
        return f"{self.home_team.name} vs {self.away_team.name} at {self.location} on {self.game_date} at {self.game_time}"

    def get_absolute_url(self):
        return reverse('schedule-detail', kwargs={'pk': self.id})


# from django.db import models
# from django.urls import reverse
# from django.utils.timezone import now
# from django.contrib.auth.models import User

# # Team Model
# class Team(models.Model):
#     name = models.CharField(max_length=255)
#     city = models.CharField(max_length=255)
#     stadium = models.CharField(max_length=255)
#     sport = models.CharField(max_length=255)
#     logo_url = models.URLField(max_length=500, blank=True, null=True)

#     def __str__(self):
#         return f"{self.name} - {self.city} - {self.stadium} - {self.sport}"
    
#     def get_absolute_url(self):
#         return reverse('team-detail', kwargs={'team_id': self.id})


# # Player Model
# class Player(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     position = models.CharField(max_length=255)
#     number = models.IntegerField()
#     team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')

#     def __str__(self):
#         return f"{self.first_name} {self.last_name} - {self.position} - #{self.number}"
    
#     def get_absolute_url(self):
#         return reverse('player-detail', kwargs={'player_id': self.id})

# # Schedule Model
# class Schedule(models.Model):
#     home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_games')
#     away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_games')
#     location = models.CharField(max_length=255)
#     game_date = models.DateField()
#     game_time = models.TimeField()
#     arena = models.TextField()

#     def __str__(self):
#         return f"{self.home_team.name} vs {self.away_team.name} at {self.location} on {self.game_date} at {self.game_time}"

#     def get_absolute_url(self):
#         return reverse('schedule-detail', kwargs={'pk': self.id})