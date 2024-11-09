from django.db import models

# Model for Player
class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    position = models.CharField(max_length=50)
    team = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Model for Game
class Game(models.Model):
    date = models.DateField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.date} at {self.location}"

# Model for PlayerStats
class PlayerStats(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    blocks = models.IntegerField(default=0)
    saves = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.player.name} Stats - {self.game.date}"
