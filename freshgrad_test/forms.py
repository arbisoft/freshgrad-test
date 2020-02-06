"""
Forms for freshgrad test
"""

from django import forms
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

from .models import CandidateInfo


class CandidateInfoForm(forms.ModelForm):
    """
    Form to gather additional info of candidate
    """
    confirm_password = forms.CharField(
        label=_("Confurm Password"),
        widget=forms.PasswordInput(attrs={'tabindex': '5'})
    )

    cnic_number = forms.CharField(
        label=_("CNIC Numbr"),
        validators=[
            RegexValidator(
                regex=r'[0-9]{5}-[0-9]{7}-[0-9]{1}',
                message="CNIC Number is not valid. CNIC number format should be 00000-0000000-0."
            )
        ],
        widget=forms.TextInput(attrs={'tabindex': '1'})
    )
    other_university = forms.CharField(
        label=_("Mention Univesity/Campus details if not present in list")
    )

    def clean_other_university(self):
        """
        Check that the user has provided the relevant information
        if the university/campus information is not present in the
        given options.
        """
        university = self.cleaned_data['university']
        campus = self.cleaned_data['campus']
        other_university = (self.cleaned_data['other_university']).strip()
        if other_university == '' and (university == 'Other' or campus == 'Other'):
            raise forms.ValidationError(_("Please provide University/Campus details."))
        return other_university

    class Meta(object):
        model = CandidateInfo
        exclude = (
            'user',
            'interested_in_python',
            'interested_in_scrappy',
            'interested_in_andriod',
            'interested_in_ios',
            'interested_in_php',
            'interested_in_javascript',
            'interested_in_machine_learning',
        )
        serialization_options = {
            'university_projects': {
                'field_type': 'textarea',
            },
            'extra_activities': {
                'field_type': 'textarea',
            },
            'freelance_work': {
                'field_type': 'textarea',
            },
            'biggest_accomplishment': {
                'field_type': 'textarea',
            },
            'makes_me_different': {
                'field_type': 'text',
            },
            'ideal_organization': {
                'field_type': 'text',
            },
            'why_arbisoft': {
                'field_type': 'textarea',
            },
            'career_plans': {
                'field_type': 'textarea',
            },
            'references': {
                'field_type': 'textarea',
            },
            'other_technologies': {
                'field_type': 'textarea',
            }

        }
