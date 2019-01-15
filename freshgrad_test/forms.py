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
    cnic_number = forms.CharField(
        label=_("CNIC Number"),
        validators=[
            RegexValidator(
                regex=r'[0-9]{5}-[0-9]{7}-[0-9]{1}',
                message="CNIC Number is not valid. CNIC number format should be 00000-0000000-0."
            )
        ]
    )

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
                'field_type': 'textarea',
            },
            'ideal_organization': {
                'field_type': 'textarea',
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
