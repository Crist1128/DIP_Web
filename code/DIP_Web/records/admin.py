from django.contrib import admin
from .models import Catalog, Diagnosis, Procedure, Scoring

admin.site.register(Catalog)
admin.site.register(Diagnosis)
admin.site.register(Procedure)
admin.site.register(Scoring)
