from django.db import models

class Card(models.Model):
    company_name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logos/')
    price_band = models.CharField(max_length=100)
    open_date = models.DateField(blank=True, null=True)
    close_date = models.DateField(blank=True, null=True)
    issue_size = models.CharField(max_length=100)
    listing_date = models.DateField(blank=True, null=True)
    rhp_drhp = models.CharField(max_length=50)  # This can be 'RHIP' or 'DHRP'

    def __str__(self):
        return self.company_name
