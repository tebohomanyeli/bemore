from django import forms
from .models import Lead

class LeadForm(forms.Form):
    first_name  :str    = forms.CharField()
    last_name   :str    = forms.CharField()
    age         :int    = forms.IntegerField(min_value=0)


# Uses the lead models template to build a table and form:
class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'age',
            'agent'
        )