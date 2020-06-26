from django.contrib import admin
from core.models import RSVPPerson, Invitation, ReservationControl

admin.site.register(RSVPPerson)
admin.site.register(Invitation)
admin.site.register(ReservationControl)
