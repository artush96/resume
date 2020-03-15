from django.contrib import admin
from .models import *
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ['id']

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id']

admin.site.register(About)
admin.site.register(AboutMe, AboutMeAdmin)
admin.site.register(Services)
admin.site.register(Pricing)
admin.site.register(Facts)
admin.site.register(Clients)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Category)
admin.site.register(Works)
admin.site.register(Blog)
admin.site.register(Experience)
admin.site.register(Skills)
admin.site.register(Education)
admin.site.register(WorkExprerience)
