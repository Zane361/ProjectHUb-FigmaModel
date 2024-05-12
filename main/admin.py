from django.contrib import admin
from . import models

admin.site.register(models.Home)
admin.site.register(models.Portfolio)
admin.site.register(models.TeamMember)
admin.site.register(models.Message)
admin.site.register(models.Vacancy)
admin.site.register(models.Resume)