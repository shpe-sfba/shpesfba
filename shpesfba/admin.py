from django.contrib import admin

# Register your models here.
from shpesfba.models import OfficerRole, Officer, Membership, Message, JobPosting, Event, MessageType, FAQ, Gallery, \
    GalleryImage

admin.site.register(OfficerRole)
admin.site.register(Officer)
admin.site.register(Membership)
admin.site.register(MessageType)
admin.site.register(Message)
admin.site.register(JobPosting)
admin.site.register(Event)
admin.site.register(FAQ)
admin.site.register(Gallery)
admin.site.register(GalleryImage)
