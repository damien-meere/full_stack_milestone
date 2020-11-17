from django.contrib import admin
from .models import SubscriberList


class SubscriberAdmin(admin.ModelAdmin):
    list_display = (
        'subscriber_id',
        'email',
    )

    ordering = ('subscriber_id',)


admin.site.register(SubscriberList, SubscriberAdmin)
