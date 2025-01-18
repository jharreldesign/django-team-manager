from django.db import models
from django.urls import reverse

from django.utils.timezone import now

# Team Model
class Team(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    stadium = models.CharField(max_length=255)
    sport = models.CharField(max_length=255)
    logo_url = models.URLField(max_length=500, blank=True, null=True)

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
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='schedules')  # Link schedule to a team
    opponent = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    game_date = models.DateField()
    game_time = models.TimeField()  # Added game time field
    arena = models.TextField()  # Allow for longer names

    def __str__(self):
        return f"{self.opponent} at {self.location} on {self.game_date} at {self.game_time}"
    
    def get_absolute_url(self):
        return reverse('schedule-detail', kwargs={'pk': self.id})


# from django.db import models
# from django.urls import reverse

# # Create your models here.

# #Team Model
# class Team(models.Model):
#     name = models.CharField(max_length=255)
#     city = models.CharField(max_length=255)
#     stadium = models.CharField(max_length=255)
#     sport = models.CharField(max_length=255)

#     def __str__(self):
#         return f"{self.name} - {self.city} - {self.stadium} - {self.sport}"
    
#     def get_absolute_url(self):
#         return reverse('team-detail', kwargs={'team_id': self.id })

# class Player(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     position = models.CharField(max_length=255)
#     number = models.IntegerField()

#     team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')

#     def __str__(self):
#         return f"{self.first_name} - {self.last_name} - {self.position} - {self.number}"
    
# class Schedule(models.Model):
#     opponent = models.CharField(max_length=255)
#     city = models.CharField(max_length=255)
#     game_date = models.DateField()
#     arena = models.CharField(max_length=255)

#     def __str__(self):
#         return f"{self.opponent} - {self.city} - {self.game_time} - {self.arena}"

#     def get_absolute_url(self):
#         return reverse('game-detail', kwargs={'pk': self.id}) 
