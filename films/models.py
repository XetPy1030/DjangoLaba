from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name


class Films(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    release_date = models.DateField()
    actors = models.CharField(max_length=100)
    show_date = models.DateField()

    def __str__(self):
        return self.name
