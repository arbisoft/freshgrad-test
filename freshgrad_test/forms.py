"""
Forms for freshgrad test
"""

from django.forms import ModelForm

from .models import CandidateInfo


class CandidateInfoForm(ModelForm):
    """
    Form to gather additional info of candidate
    """

    class Meta(object):
        model = CandidateInfo
        exclude = ('user', )
