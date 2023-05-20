from django.contrib import admin

from producer.gear import ActTechRider, Instrument, Microphone
from producer.models import Performance
from producer.people import Act, Person, Role
from producer.show import Show


@admin.register(Person, Role)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(ActTechRider)
class ActTechAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    ...

@admin.register(Act, Instrument, Microphone)
class ActAdmin(admin.ModelAdmin):
    ...


@admin.register(Performance, Show)
class PerformanceAdmin(admin.ModelAdmin):
    exclude = ('slug',)
