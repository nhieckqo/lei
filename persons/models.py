from django.db import models

# Create your models here.
class Persons(models.Model):
    p_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=200, blank=True, null=True)
    midname = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(max_length=200, blank=True, null=True)
    fullname = models.TextField(blank=True, null=True)
    organization_name = models.CharField(max_length=400, blank=True, null=True)
    fulladdress = models.TextField(blank=True, null=True)
    address_num = models.CharField(max_length=100, blank=True, null=True)
    address_street = models.CharField(max_length=500, blank=True, null=True)
    address_lot = models.CharField(max_length=100, blank=True, null=True)
    address_block = models.CharField(max_length=100, blank=True, null=True)
    address_phase = models.CharField(max_length=100, blank=True, null=True)
    address_sitio = models.CharField(max_length=500, blank=True, null=True)
    address_brgy = models.CharField(max_length=100, blank=True, null=True)
    address_city = models.CharField(max_length=100, blank=True, null=True)
    address_province = models.CharField(max_length=100, blank=True, null=True)
    address_country = models.CharField(max_length=100, blank=True, null=True)
    address_zipcode = models.CharField(max_length=100, blank=True, null=True)
    contact_no = models.CharField(max_length=100, blank=True, null=True)
    contact_no_cp = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    sex_types_id = models.IntegerField(blank=True, null=True)
    profile_share_types_id = models.IntegerField(blank=True, null=True)
    tin = models.CharField(max_length=100, blank=True, null=True)
    profession = models.CharField(max_length=200, blank=True, null=True)
    work_income = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    citizenship = models.CharField(max_length=100, blank=True, null=True)
    birthplace = models.CharField(max_length=200, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    height = models.CharField(max_length=50, blank=True, null=True)
    weight = models.CharField(max_length=50, blank=True, null=True)
    civil_status_id = models.IntegerField(blank=True, null=True)
    pok_organization_kind_code = models.ForeignKey('PersonsOrganizationKinds',
        models.DO_NOTHING, db_column='pok_organization_kind_code', blank=True, null=True,
        to_field='organization_kind_code')
    grp_place_of_registration = models.TextField(blank=True, null=True)
    grp_date_of_registration = models.DateField(blank=True, null=True)
    grp_nature_of_business = models.TextField(blank=True, null=True)
    grp_organization_branch = models.TextField(blank=True, null=True)
    timestamp_created = models.DateTimeField(blank=True, null=True)
    pt_persons_types_code = models.ForeignKey('PersonsTypes', models.DO_NOTHING,
        db_column='pt_persons_types_code', blank=True, null=True, to_field="persons_types_code")
    pst_sex_types_code = models.ForeignKey('PersonsSexTypes', models.DO_NOTHING,
        db_column='pst_sex_types_code', blank=True, null=True, to_field='sex_types_code')
    ppst_profile_share_types_code = models.ForeignKey('PersonsProfileShareTypes',
        models.DO_NOTHING, db_column='ppst_profile_share_types_code', blank=True,
        null=True, to_field='profile_share_types_code')
    pcs_civil_status_code = models.ForeignKey('PersonsCivilStatus', models.DO_NOTHING,
        db_column='pcs_civil_status_code', blank=True, null=True,  to_field='civil_status_code')

    class Meta:
        managed = False
        db_table = 'persons'

    def __str__(self):
        return self.lastname + ", " +self.firstname+ " " +self.midname+ " " +self.organization_name

class PersonsCedula(models.Model):
    pc_id = models.AutoField(primary_key=True)
    persons_p = models.ForeignKey(Persons, models.DO_NOTHING, blank=True, null=True)
    cedula_no = models.CharField(max_length=100, blank=True, null=True)
    cedula_date = models.DateField(blank=True, null=True)
    cedula_place = models.CharField(max_length=500, blank=True, null=True)
    is_issued_here = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persons_cedula'


class PersonsCivilStatus(models.Model):
    pcs_id = models.AutoField(primary_key=True)
    civil_status_code = models.CharField(unique=True, max_length=100, blank=True, null=True)
    civil_status_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persons_civil_status'

    def __str__(self):
        return self.civil_status_code

class PersonsFieldStatus(models.Model):
    pfs_id = models.AutoField(primary_key=True)
    enabled = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persons_field_status'


class PersonsFieldTypes(models.Model):
    pft_id = models.AutoField(primary_key=True)
    field_types_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persons_field_types'


class PersonsFields(models.Model):
    pf_id = models.AutoField(primary_key=True)
    fields_name = models.CharField(max_length=200, blank=True, null=True)
    pft_field_types = models.ForeignKey(PersonsFieldTypes, models.DO_NOTHING, blank=True,
        null=True)
    pfs_field_status = models.ForeignKey(PersonsFieldStatus, models.DO_NOTHING, blank=True,
        null=True)
    m_module_code = models.ForeignKey('PersonsModules', models.DO_NOTHING,
        db_column='m_module_code', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persons_fields'


class PersonsFieldsAdditional(models.Model):
    pfa_id = models.AutoField(primary_key=True)
    persons = models.ForeignKey(Persons, models.DO_NOTHING, blank=True, null=True)
    fields = models.ForeignKey(PersonsFields, models.DO_NOTHING, blank=True, null=True)
    text_val = models.TextField(blank=True, null=True)
    numeric_val = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    date_val = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persons_fields_additional'


class PersonsHiddenFields(models.Model):
    phf_id = models.AutoField(primary_key=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    hide_status = models.BooleanField(blank=True, null=True)
    widget_name = models.CharField(max_length=100, blank=True, null=True)
    m_module_code = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persons_hidden_fields'


class PersonsModules(models.Model):
    pm_id = models.AutoField(primary_key=True)
    mod_code = models.CharField(unique=True, max_length=100, blank=True, null=True)
    module_name = models.CharField(max_length=200, blank=True, null=True)
    system_code = models.ForeignKey('Systems', models.DO_NOTHING, db_column='system_code',
        blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persons_modules'


class PersonsOrganizationKinds(models.Model):
    pok_id = models.AutoField(primary_key=True)
    organization_kind_description = models.TextField(blank=True, null=True)
    organization_kind_code = models.CharField(unique=True, max_length=100, blank=True,
        null=True)

    class Meta:
        managed = False
        db_table = 'persons_organization_kinds'

    def __str__(self):
            return self.organization_kind_code


class PersonsOrganizationMembers(models.Model):
    pom_id = models.AutoField(primary_key=True)
    organizations_p = models.ForeignKey(Persons, models.DO_NOTHING, blank=True, null=True)
    persons_p = models.IntegerField(blank=True, null=True)
    pmt_membership_types_code = models.ForeignKey('PersonsOrganizationMembershipTypes',
        models.DO_NOTHING, db_column='pmt_membership_types_code', blank=True, null=True)
    temp_membership_types_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persons_organization_members'


class PersonsOrganizationMembershipTypes(models.Model):
    pmt_id = models.AutoField(primary_key=True)
    membership_types_code = models.CharField(unique=True, max_length=100, blank=True, null=True)
    membership_types_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persons_organization_membership_types'


class PersonsProfileShareGroups(models.Model):
    ppsg_id = models.AutoField(primary_key=True)
    m_module_code = models.ForeignKey(PersonsModules, models.DO_NOTHING,
        db_column='m_module_code', blank=True, null=True)
    access_rights = models.BooleanField(blank=True, null=True)
    ppst_profile_share_types_code = models.ForeignKey('PersonsProfileShareTypes',
        models.DO_NOTHING, db_column='ppst_profile_share_types_code', blank=True, null=True)
    is_default_share_type = models.BooleanField(blank=True, null=True)
    temp_profile_share_types_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persons_profile_share_groups'


class PersonsProfileShareTypes(models.Model):
    ppst_id = models.AutoField(primary_key=True)
    profile_share_types_code = models.CharField(unique=True, max_length=100, blank=True,
        null=True)
    profile_share_types_name = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persons_profile_share_types'

    def __str__(self):
        return self.profile_share_types_code

class PersonsSexTypes(models.Model):
    pst_id = models.AutoField(primary_key=True)
    sex_types_code = models.CharField(unique=True, max_length=100, blank=True, null=True)
    sex_types_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persons_sex_types'

    def __str__(self):
        return self.sex_types_code

class PersonsTypes(models.Model):
    pt_id = models.AutoField(primary_key=True)
    persons_types_name = models.CharField(max_length=400, blank=True, null=True)
    persons_types_code = models.CharField(unique=True, max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persons_types'

    def __str__(self):
        return self.persons_types_code

class Systems(models.Model):
    sys_id = models.AutoField(primary_key=True)
    sys_code = models.CharField(unique=True, max_length=100)
    systems_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'systems'
