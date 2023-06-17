from django.contrib import admin
from SM.models import experiments,Contactus

# Register your models here.
class experimentsAdmin(admin.ModelAdmin):
    list_display = ('exp_name','subject_name','sem_num','exp_file')
admin.site.register(experiments,experimentsAdmin)


class contactusAdmin(admin.ModelAdmin):
    list_display = ('name','email','msg')
admin.site.register(Contactus,contactusAdmin)