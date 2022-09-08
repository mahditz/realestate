from django.contrib import admin
from . import models

admin.site.site_header= "مشاور املاک الماس اکباتان "
admin.site.site_title= "الماس اکباتان  "

class RentAdmin(admin.ModelAdmin):
    list_display = ('code','nameM','melktype', 'metraj','phase','priceR','area','date','status')
    list_filter = ('melktype','area','phase','date','relname','status')
    search_fields = ['code','nameM']
    readonly_fields = ['relname']
    
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        return self.readonly_fields

    def has_change_permission(self, request, obj=None):
        if not request.user.is_superuser :
            if obj is not None and obj.relname != request.user:
                return False
        return True
    
    def has_delete_permission(self, request, obj=None):
        if not request.user.is_superuser :
            if obj is not None and obj.relname != request.user:
                return False
        return True
        
    def save_model(self, request, instance, form, change):
        instance = form.save(commit=False)
        if not request.user.is_superuser :
            instance.relname = request.user
        instance.save()
        form.save_m2m()
        return instance

admin.site.register(models.rent,RentAdmin)

class SellAdmin(admin.ModelAdmin):
    list_display = ('code','nameM','melktype','metraj','area','phase','priceM','block','date','status')
    list_filter = ('melktype','area','phase','date','relname','status')
    search_fields = ['code','nameM']
    readonly_fields = ['relname']
    
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        return self.readonly_fields

    def has_change_permission(self, request, obj=None):
        if not request.user.is_superuser :
            if obj is not None and obj.relname != request.user:
                return False
        return True
    
    def has_delete_permission(self, request, obj=None):
        if not request.user.is_superuser :
            if obj is not None and obj.relname != request.user:
                return False
        return True
        
    def save_model(self, request, instance, form, change):
        instance = form.save(commit=False)
        instance.relname = request.user 
        instance.save()
        form.save_m2m()
        return instance


admin.site.register(models.sell,SellAdmin)
admin.site.register(models.Area)

