# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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

    class Meta:
        managed = False
        db_table = 'lei"."cfg_certifying_officers'

    def __str__(self):
        return str(self.name)


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
        return str(self.name)


class LegApprovedBy(models.Model):
    li_lab_id = models.AutoField(primary_key=True)
    approved_by_name = models.TextField(blank=True, null=True)
    approved_by_designation = models.TextField(blank=True, null=True)
    approved_by_remarks = models.TextField(blank=True, null=True)
    li_li = models.ForeignKey('LegislativeInfo', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lei"."leg_approved_by'

    def __str__(self):
        return str(self.approved_by_name)


class LegAttendees(models.Model):
    li_la_id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    designation = models.TextField(blank=True, null=True)
    is_present = models.BooleanField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    li_li = models.ForeignKey('LegislativeInfo', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lei"."leg_attendees'

    def __str__(self):
        return str(self.name)


class LegAttestedBy(models.Model):
    li_lab_id = models.AutoField(primary_key=True)
    attested_by_name = models.TextField(blank=True, null=True)
    attested_by_designation = models.TextField(blank=True, null=True)
    attested_by_remarks = models.TextField(blank=True, null=True)
    li_li = models.ForeignKey('LegislativeInfo', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lei"."leg_attested_by'

    def __str__(self):
        return str(self.attested_by_name)


class LegCertifiedBy(models.Model):
    li_lcb_id = models.AutoField(primary_key=True)
    certified_by_name = models.TextField(blank=True, null=True)
    certified_by_designation = models.TextField(blank=True, null=True)
    certified_by_remarks = models.TextField(blank=True, null=True)
    li_li = models.ForeignKey('LegislativeInfo', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lei"."leg_certified_by'

    def __str__(self):
        return str(self.certified_by_name)


class LegPresidedOverBy(models.Model):
    li_lpob_id = models.AutoField(primary_key=True)
    presided_over_by_name = models.TextField(blank=True, null=True)
    presided_over_by_designation = models.TextField(blank=True, null=True)
    presided_over_by_remarks = models.TextField(blank=True, null=True)
    li_li = models.ForeignKey('LegislativeInfo', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lei"."leg_presided_over_by'

    def __str__(self):
        return str(self.presided_over_by_name)


class LegislativeInfo(models.Model):
    li_id = models.AutoField(primary_key=True)
    record_no = models.CharField(max_length=100, blank=True, null=True)
    series = models.CharField(max_length=100, blank=True, null=True)
    approved_date = models.DateField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    body_text = models.TextField(blank=True, null=True)
    created_by_username = models.CharField(max_length=100, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    edited_date = models.DateTimeField(blank=True, null=True)
    edited_by_username = models.CharField(max_length=100, blank=True, null=True)
    whole_text = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    scanned = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lei"."legislative_info'

    def __str__(self):
        return str(self.record_no)+" - "+str(self.title)


class OverviewLi(models.Model):
    li_id = models.IntegerField(blank=True, null=True)
    res_no_full = models.TextField(blank=True, null=True)
    approved_date = models.DateField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    scanned = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'lei"."overview__li'
