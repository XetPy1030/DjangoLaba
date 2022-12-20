from django.contrib import admin
from .models import Category, Films

admin.site.register([Category, Films])