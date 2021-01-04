from django.db import models

# Skill Model
class Skill(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

# Job Model
class Job(models.Model):
    title = models.CharField(max_length=50)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# Candidate Model
class Candidate(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.name + ", " + self.title