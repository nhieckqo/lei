from django.db import models

# Create your models here.
class CfgApprovingOfficers(models.Model):
    li_ao_id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    designation = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lei"."cfg_approving_officers'

    def __str__(self):
        return str(self.name)


class CfgAttestingOfficers(models.Model):
    li_ao_id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    designation = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lei"."cfg_attesting_officers'

    def __str__(self):
        return str(self.name)


class CfgCertifyingOfficers(models.Model):
    li_co_id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    designation = models.TextField(blank=True, null=True)
    co_code = models.CharField(max_length=100, unique=True)

    class Meta:
        managed = False
        db_table = 'lei"."cfg_certifying_officers'

    def __str__(self):
        return str(self.name) + " - " + str(self.designation)


class CfgGlobal(models.Model):
    li_cg_id = models.AutoField(primary_key=True)
    attribute_name = models.CharField(max_length=200, blank=True, null=True)
    val_text = models.TextField(blank=True, null=True)
    val_num = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    val_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lei"."cfg_global'

    def __str__(self):
        return str(self.attribute_name)


class CfgOfficials(models.Model):
    li_o_id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    designation = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lei"."cfg_officials'

    def __str__(self):
        return str(self.name)


class CfgPresidingOfficers(models.Model):
    li_po_id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    designation = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lei"."cfg_presiding_officers'

    def __str__(self):
        return str(self.name) + " - " + str(self.designation)
