from django.contrib import admin

# Register models.
from .models import Concert

admin.site.register(Concert)
