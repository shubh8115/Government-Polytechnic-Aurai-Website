from django.contrib import admin

# Register your models here.
from .models import *
class tblcontactAdmin(admin.ModelAdmin):
    list_display=("id","name","email","mobile","message")

admin.site.register(tblcontact,tblcontactAdmin)


class tblgalleryAdmin(admin.ModelAdmin):
    list_display=( "id", "title","picture")

admin.site.register(tblgallery,tblgalleryAdmin)   

class tblplacementsAdmin(admin.ModelAdmin):
    list_display=("id","name","picture","psession","company","designation")

admin.site.register(tblplacements,tblplacementsAdmin)        


class tblbranchAdmin(admin.ModelAdmin):
    list_display=("id","name","no_of_seats","picture")

admin.site.register(tblbranch,tblbranchAdmin)  


class tblteamAdmin(admin.ModelAdmin):
    list_display=("id","name","designation","picture")

admin.site.register(tblteam,tblteamAdmin)  




class tblfacilitiesAdmin(admin.ModelAdmin):
    list_display=("id","title","description","picture")

admin.site.register(tblfacilities,tblfacilitiesAdmin)   


class newAdmin(admin.ModelAdmin):
    list_display=("id","title","posted_date")
admin.site.register(new,newAdmin)    
