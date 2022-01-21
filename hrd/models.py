from django.db import models


class team(models.Model):
    team_name = models.CharField(max_length=30)
    team_position = models.CharField(max_length=100)
    team_explanation = models.TextField()


    def __str__(self):
        return f'[{self.pk}]{self.team_name}'
