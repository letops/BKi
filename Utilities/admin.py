from django.contrib import admin
from Utilities import models

admin.site.register(models.UtilityType)
admin.site.register(models.Utility)
admin.site.register(models.PoliticalAreaType)
admin.site.register(models.PoliticalArea)
admin.site.register(models.PoliticalAreaUtility)
admin.site.register(models.Zip)
