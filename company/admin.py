from django.contrib import admin
from company.models import *

# Register your models here.
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "status",)
    search_fields = ("name", "position__name", "email",)
    list_filter = ("position", "status", )
    ordering = ("email", )
    
    class Media:
        pass

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ("name", "zone", "url", )
    search_fields = ("name", "url", )
    list_filter = ("zone", )
    
    class Media:
        pass

@admin.register(Share)
class ShareAdmin(admin.ModelAdmin):
	list_display = ("person", "topic", "created",)
	search_fields = ("person__name", "topic",)
	ordering = ("created",)
	date_hierarchy = 'created'

	class Media:
		pass

@admin.register(MacAddr)
class MacAddrAdmin(admin.ModelAdmin):
	list_display = ("person", "wire_ip", "wire_mac", "wire_less_ip", "wire_less_mac", )
	search_fields = ("person__name", "has_pro_pm", )
	ordering = ("person__name", )
	class Media:
		pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ("name", "author", "cat", "owner", "status", )
	search_fields = ("name", "author", )
	list_filter = ("cat__name", "owner__name", "status",)
	ordering = ("name",)
	class Media:
		pass

admin.site.register(Position)
admin.site.register(Zone)
admin.site.register(BookCat)
