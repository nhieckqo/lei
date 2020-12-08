from django import forms

from . import models


class LegislativeInfoForm(forms.ModelForm):

    class Meta:
        model = models.LegislativeInfo
        fields = ['record_no', 'series', 'approved_date', 'title', 'summary', 'body_text',]


class LegPresidedOverByForm(forms.ModelForm):

    class Meta:
        model = models.LegPresidedOverBy
        fields = ['li_li_po']

    def __init__(self, *args, **kwargs):
        super(LegPresidedOverByForm, self).__init__(*args, **kwargs)
        self.fields['li_li_po'] = forms.ModelChoiceField(queryset=models.CfgPresidingOfficers.objects,
                                                                            label="Presiding Officer")
