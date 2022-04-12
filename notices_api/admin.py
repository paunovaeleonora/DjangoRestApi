from django.contrib import admin


from notices_api.models import Notices


@admin.register(Notices)
class NoticesAdmin(admin.ModelAdmin):
    search_fields = ('notice_date', 'notice_number',)


