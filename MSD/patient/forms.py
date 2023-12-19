from django import forms

from .models import Patient
from account.models import User


class PatientForm(forms.ModelForm):
    doctors = forms.ModelMultipleChoiceField(queryset=User.objects.filter(role='DR'), required=False)
    nurses = forms.ModelMultipleChoiceField(queryset=User.objects.filter(role='NR'), required=False)

    class Meta:
        model = Patient
        fields = ('first_name', 'last_name', 'gender', 'street', 'house_number', 'postal_code', 'city', 'phone',
                  'date_of_birth', 'email', 'doctors', 'nurses', 'reason_of_visiting')
