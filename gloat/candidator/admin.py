from django.contrib import admin

from .models import Skill, Job, Candidate

# Reset Admin Titles
admin.site.site_header = "Gloat Home Assignment App"
admin.site.site_title = "Admin Dashboard"
admin.site.index_title = "Welcome To Gloat's Job Finder"

# Register models to admin panel
admin.site.register(Skill)
admin.site.register(Job)
admin.site.register(Candidate)