from django.contrib import admin
from .models import ProviderAndCountry, ColumbiaData, DRFData
# Register your models here.

admin.site.register(ProviderAndCountry)
admin.site.register(ColumbiaData)
admin.site.register(DRFData)
