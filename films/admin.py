from django.contrib import admin
from .models import Category, Film

admin.site.register([Category, Film])