"""
Forms for freshgrad test
"""

from django import forms
from django.utils.translation import gettext_lazy as _

from .models import CandidateInfo


class CandidateInfoForm(forms.ModelForm):
    """
    Form to gather additional info of candidate
    """
    # Have to define these fields in the form to avoid these fields being displayed
    # in optional fields at the bottom of registration form
    YES_NO = (
        ('', ''),
        (0, 'No'),
        (1, 'Yes'),
    )
    interested_in_python = forms.ChoiceField(label=_("Interested in Python/Django"), choices=YES_NO)
    interested_in_scrappy = forms.ChoiceField(label=_("Interested in Scrappy"), choices=YES_NO)
    interested_in_andriod = forms.ChoiceField(label=_("Interested in Android"), choices=YES_NO)
    interested_in_ios = forms.ChoiceField(label=_("Interested in iOS"), choices=YES_NO)
    interested_in_php = forms.ChoiceField(label=_("Interested in PHP"), choices=YES_NO)
    interested_in_javascript = forms.ChoiceField(label=_("Interested in Javascript/ReactJS"), choices=YES_NO)
    interested_in_machine_learning = forms.ChoiceField(label=_("Interested in Machine Learning"), choices=YES_NO)

    class Meta(object):
        model = CandidateInfo
        exclude = ('user', )
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

        }
