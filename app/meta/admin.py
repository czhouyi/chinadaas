from django.contrib import admin
from models import *

# Register your models here.
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
	list_display = ("cat", "name", "alias",)
	search_fields = ("cat__name", "name", "alias",)
	list_filter = ("cat",)
	ordering = ("name",)

	class Media:
		pass

@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
	list_display = ("table", "name", "alias", "type", )
	search_fields = ("table__name", "name", "alias", )
	list_filter = ("table", )
	ordering = ("name",)

	class Media:
		pass

admin.site.register(TableCat)
