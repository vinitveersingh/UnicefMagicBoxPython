from django.db import models

# Create your models here.
class ProviderAndCountry(models.Model):
    provider=models.CharField(max_length=256, primary_key=True)
    country=models.CharField(max_length=256)
    country_code=models.CharField(max_length=256)

class ColumbiaData(models.Model):
    provider_country=models.ForeignKey(ProviderAndCountry, on_delete=models.CASCADE)
    date=models.DateField()
    created_at=models.DateField()
    updated_at=models.DateField()
    id_origin=models.CharField(max_length=256)
    id_destination=models.CharField(max_length=256)
    journeys=models.IntegerField()
    people=models.IntegerField()
    shapefile=models.CharField(max_length=256)

class DRFData(models.Model):
    provider_country=models.ForeignKey(ProviderAndCountry, on_delete=models.CASCADE)
    date=models.DateField()
    created_at=models.DateField()
    updated_at=models.DateField()
    id_origin=models.CharField(max_length=256)
    id_destination=models.CharField(max_length=256)
    journeys=models.IntegerField()
    people=models.IntegerField()
    shapefile=models.CharField(max_length=256)
