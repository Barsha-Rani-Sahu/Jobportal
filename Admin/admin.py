from django.contrib import admin # type: ignore
from Admin.models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('Category_name',)



admin.site.register(Category,CategoryAdmin)

