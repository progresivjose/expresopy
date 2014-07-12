from django.contrib import admin
from .models import Editorial

# Register your models here.
class EditorialAdmin(admin.ModelAdmin):
	list_display = ('title', 'created', 'show_tags', 'user')
	fields = ['title', 'summary', 'text', 'tags']

	def show_tags(self, obj):
		tags = obj.tags.names()
		return ",".join(tags)

	def save_model(self, request, editorial, form, change):
		editorial.user = request.user
		editorial.save()

admin.site.register(Editorial, EditorialAdmin)
