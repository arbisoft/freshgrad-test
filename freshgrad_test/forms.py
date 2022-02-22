"""
Forms for freshgrad test
"""

from django import forms
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _

from .models import CandidateInfo


class CandidateInfoForm(forms.ModelForm):
    """
    Form to gather additional info of candidate
    """
    confirm_password = forms.CharField(
        label=_("Confirm Password"),
        widget=forms.PasswordInput(attrs={'tabindex': '5'})
    )

    cnic_number = forms.CharField(
        label=_("CNIC Number"),
        validators=[
            RegexValidator(
                regex=r'[0-9]{5}-[0-9]{7}-[0-9]{1}',
                message="CNIC Number is not valid. CNIC number format should be 00000-0000000-0."
            )
        ],
        widget=forms.TextInput(attrs={'tabindex': '1'})
    )

    contact_number = forms.CharField(
        label='Contact Number(s)',
        validators=[
            RegexValidator(
                regex=r'^[0-9]+$',
                message="Contact Number is not valid. Contact Number format should be digits only."
            )
        ]
    )

    age = forms.CharField(
        label="Age (between 18 to 30)",
        validators=[
            RegexValidator(
                regex=r'^(1[9]|2[0-9]|3[01])$',
                message="Age is not valid. Age should be between 18 to 30."
            )
        ]
    )

    expected_salary = forms.CharField(
        label="Your salary expections?"
    )
    graduation_date = forms.CharField(
        label="Expected Graduation Date"
    )

    # other_university = forms.CharField(
    #     label=_("Mention Univesity/Campus details if not present in list (optional)")
    # )

    # def clean_other_university(self):
    #     """
    #     Check that the user has provided the relevant information
    #     if the university/campus information is not present in the
    #     given options.
    #     """
    #     university = self.cleaned_data['university']
    #     campus = self.cleaned_data['campus']
    #     other_university = (self.cleaned_data['other_university']).strip()
    #     if other_university == '' and (university == 'Other' or campus == 'Other'):
    #         raise forms.ValidationError(_("Please provide University/Campus details."))
    #     return other_university

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
            'university',
            'campus',
            'other_university',
            'city',
            'graduation_date',
        )
        serialization_options = {
            # 'university_projects': {
            #     'field_type': 'textarea',
            # },
            # 'extra_activities': {
            #     'field_type': 'text',
            # },
            # 'freelance_work': {
            #     'field_type': 'text',
            # },
            # 'biggest_accomplishment': {
            #     'field_type': 'text',
            # },
            'makes_me_different': {
                'field_type': 'text',
            },
            'ideal_organization': {
                'field_type': 'text',
            },
            'why_arbisoft': {
                'field_type': 'text',
            },
            'career_plans': {
                'field_type': 'text',
            },
            'references': {
                'field_type': 'textarea',
            },
            # 'other_technologies': {
            #     'field_type': 'textarea',
            # }

        }
