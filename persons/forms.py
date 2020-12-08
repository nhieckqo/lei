from django import forms

from .  import models


class PersonsForm(forms.ModelForm):

    class Meta:
        model = models.Persons
        # fields = '__all__'
        exclude = ['p_id', 'sex_types_id', 'profile_share_types_id', 'civil_status_id',
                        'timestamp_created', 'fullname', 'fulladdress']
