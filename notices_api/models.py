from django.db import models


# Create your models here.

class Notices(models.Model):
    notice_number = models.TextField(primary_key=True)
    notice_date = models.TextField(blank=True, null=True)
    tender_name = models.TextField(blank=True, null=True)
    procedure_state = models.TextField(blank=True, null=True)
    contract_type = models.TextField(blank=True, null=True)
    procedure_type = models.TextField(blank=True, null=True)
    estimated_value = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.tender_name

    class Meta:
        managed = False
        db_table = 'notices'
