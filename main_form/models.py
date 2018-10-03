from django.db import models


# Create your models here.

class planet(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class jedi_bd(models.Model):
    name = models.CharField(max_length=100)
    planet = models.ForeignKey(planet, on_delete=models.DO_NOTHING)
    order_code = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


class padawan_bd(models.Model):
    name = models.CharField(max_length=100)
    planet = models.ForeignKey(planet, on_delete=models.DO_NOTHING)
    age = models.PositiveSmallIntegerField()
    email = models.EmailField()
    name_jedi = models.ForeignKey(jedi_bd, on_delete=models.DO_NOTHING)
    order_code = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class candidate(models.Model):
    name = models.CharField(max_length=100)
    planet = models.ForeignKey(planet, on_delete=models.DO_NOTHING)
    age = models.PositiveSmallIntegerField()
    email = models.EmailField(unique=True)
    answers = models.TextField(blank=True, default='')

    def __str__(self):
        return self.name


class test(models.Model):
    question = models.CharField(max_length=100)
    answer = models.BooleanField()

    def __str__(self):
        return self.question
