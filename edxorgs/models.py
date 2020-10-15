from django.db import models

# Create your models here.


class OrganizationsOrganization(models.Model):
    created = models.DateTimeField()
    modified = models.DateTimeField()
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    logo = models.CharField(max_length=255, blank=True, null=True)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'organizations_organization'
