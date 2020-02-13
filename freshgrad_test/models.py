"""
Database Models
"""
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from .constants import CAMPUS, UNIVERSITIES

# Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


# class Course(models.Model):
#     """
#     Courses candidate studied by candidate
#     """
#     name = models.CharField(max_length=100)


# class Technology(models.Model):
#     """
#     Technologies candidate would like to learn or work on
#     """
#     name = models.CharField(max_length=100)


class CandidateInfo(models.Model):
    """
    This model contains two extra fields that will be saved when a user registers.
    """
    user = models.OneToOneField(USER_MODEL)
    confirm_password = models.CharField(max_length=50, blank=True)
    cnic_number = models.CharField(max_length=20, verbose_name=_("CNIC Number"))
    age = models.CharField(max_length=2, verbose_name=_("Age (between 18 to 30)"))
    university = models.CharField(max_length=100, choices=UNIVERSITIES)
    campus = models.CharField(max_length=30, choices=CAMPUS)
    other_university = models.CharField(
        max_length=50, blank=True, verbose_name=_("University details, if not in list")
    )
    city = models.CharField(max_length=30, verbose_name=_("Your current Location (City)"))
    address = models.CharField(max_length=255, verbose_name=_("Permanent Address"))
    contact_number = models.CharField(max_length=30, verbose_name=_("Contact Number(s)"))
    graduation_date = models.CharField(max_length=20, verbose_name=_("Expected Graduation Date"))
    cgpa = models.CharField(max_length=10, verbose_name=_("CGPA"))
    position = models.CharField(max_length=20, verbose_name=_("Position in class"))

    # since edx custom registeration forms don't support manytomany fields
    # we have to created these boolean fields for technologies
    interested_in_python = models.BooleanField(default=False, verbose_name=_("Interested in Python/Django"))
    interested_in_scrappy = models.BooleanField(default=False, verbose_name=_("Interested in Scrappy"))
    interested_in_andriod = models.BooleanField(default=False, verbose_name=_("Interested in Android"))
    interested_in_ios = models.BooleanField(default=False, verbose_name=_("Interested in iOS"))
    interested_in_php = models.BooleanField(default=False, verbose_name=_("Interested in PHP"))
    interested_in_javascript = models.BooleanField(default=False, verbose_name=_("Interested in Javascript/ReactJS"))
    interested_in_machine_learning = models.BooleanField(
        default=False, verbose_name=_("Interested in Machine Learning")
    )

    # courses_studied = models.ManyToManyField(
    #     Course, through='CourseExpertLevel', verbose_name=_("Choose the courses you studied and your expert level")
    # )
    #
    # other_courses = models.CharField(
    #     max_length=100, null=True, blank=True, verbose_name=_("Other Courses Studied and expert level")
    # )
    # technologies_interested = models.ManyToManyField(
    #     Technology, verbose_name=_("Choose the technologies you are interested to work on/learn")
    # )
    other_technologies = models.TextField(
        verbose_name=_("Which technologies are you interested to work in? (Python/Django, Scrapy, Android, iOS, "
                       "PHP, Javascript/ReactJS, Machine Learning)")
    )
    university_projects = models.TextField(verbose_name=_("Tell us something about your university project(s)"))
    extra_activities = models.TextField(
        verbose_name=_("List down any extra curricular activitiez you're involved in(if any)? (100 characters at max)"),
        max_length=100
    )
    freelance_work = models.TextField(
        verbose_name=_("Mention any freelance work you do/have done? (200 characters at max)"),
        max_length=200
    )
    biggest_accomplishment = models.TextField(
        verbose_name=_("Your biggest acomplishment to-date? (200 characters at max)"),
        max_length=200
    )
    makes_me_different = models.CharField(
        verbose_name=_("What makes you different from your batch mates?"),
        max_length=20
    )
    ideal_organization = models.CharField(
        verbose_name=_("Describe your ideal organization? (50 characters at max)"),
        max_length=51
    )
    why_arbisoft = models.TextField(
        verbose_name=_("Why Arbisoft? (50 characters at max)"),
        max_length=50
    )
    expected_salary = models.TextField(
        verbose_name=_("Your salary expectations?")
    )
    career_plans = models.TextField(
        verbose_name=_("Your career plans two years down the line? (100 characters at max)"),
        max_length=100,
        blank=True
    )
    references = models.TextField(
        verbose_name=_("Mention two university references along with their position and contact number"),
        blank=True
    )


# class CourseExpertLevel(models.model):
#     EXPERT_LEVELS_CHOICES = (
#         (1, 'Least Expert'),
#         (2, 'Mediocre'),
#         (3, 'Expert'),
#     )
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     candidate = models.ForeignKey(CandidateInfo, on_delete=models.CASCADE)
#     expert_level = models.SmallIntegerField(choices=EXPERT_LEVELS_CHOICES)
