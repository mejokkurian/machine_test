from django.contrib import admin

# Register your models here.
from .models import choices_and_answers,quiz

admin.site.register(choices_and_answers)
admin.site.register(quiz)

