from django.contrib import admin
from models import *

# Register your models here.
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("user", )
    search_fields = ("user__username", "user__email",)
    ordering = ("user__email", )
    class Media:
        pass


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ("name", "domain", "url", )
    search_fields = ("name", "url", )
    list_filter = ("domain", )
    class Media:
        pass


@admin.register(Share)
class ShareAdmin(admin.ModelAdmin):
	list_display = ("person", "topic", "created",)
	search_fields = ("person__user__username", "topic",)
	ordering = ("created",)
	date_hierarchy = 'created'
	class Media:
		pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ("name", "author", "cat", "owner", "status", )
	search_fields = ("name", "author", )
	list_filter = ("cat__name", "owner__user__username", "status",)
	ordering = ("name",)
	class Media:
		pass


admin.site.register(Domain)
admin.site.register(BookCat)
