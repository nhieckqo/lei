from django.contrib import admin
from . import models

# Register your models here.


admin.site.register(models.CfgApprovingOfficers)
admin.site.register(models.CfgAttestingOfficers)
admin.site.register(models.CfgCertifyingOfficers)
admin.site.register(models.CfgGlobal)
admin.site.register(models.CfgOfficials)
admin.site.register(models.CfgPresidingOfficers)
admin.site.register(models.LegApprovedBy)
admin.site.register(models.LegAttendees)
admin.site.register(models.LegAttestedBy)
admin.site.register(models.LegCertifiedBy)
admin.site.register(models.LegPresidedOverBy)
admin.site.register(models.LegislativeInfo)
