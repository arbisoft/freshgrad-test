import csv

from django.contrib import admin
from django.http import HttpResponse

from .models import CandidateInfo


@admin.register(CandidateInfo)
class CandidateInfoAdmin(admin.ModelAdmin):
    list_display = (
        'user_email_view',
        'user_full_name_view',
        'cnic_number',
        'university',
        'contact_number',
    )
    list_filter = ('university', )
    search_fields = ('user__email', 'cnic_number', )

    def user_email_view(self, obj):
        return obj.user.email

    def user_full_name_view(self, obj):
        return obj.user.profile.name

    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        excluded_fields = [
            'id',
            'user',
            'interested_in_python',
            'interested_in_scrappy',
            'interested_in_andriod',
            'interested_in_ios',
            'interested_in_php',
            'interested_in_javascript',
            'interested_in_machine_learning',
        ]
        model_field_names = [field.name for field in meta.fields if field.name not in excluded_fields]

        addl_field_names = ['email', 'name']

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(addl_field_names + model_field_names)
        for obj in queryset:
            model_field_data = [getattr(obj, field) for field in model_field_names]
            addl_field_data = [obj.user.email, obj.user.profile.name]
            writer.writerow([data.encode("utf-8") for data in addl_field_data + model_field_data])

        return response

    export_as_csv.short_description = 'Export Selected'
    user_email_view.short_description = 'Email Address'
    user_full_name_view.short_description = 'Full Name'

    actions = ["export_as_csv"]
