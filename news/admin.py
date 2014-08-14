from django.contrib import admin
from .models import New

# Register your models here.
class NewAdmin(admin.ModelAdmin):
	list_display = ('title', 'category','created', 'show_tags', 'user')
	fields = ['title', 'summary', 'text', 'category', 'image', 'tags']

	def show_tags(self, obj):
		tags = obj.tags.names()
		return ",".join(tags)

	def save_model(self, request, new, form, change):
		new.user = request.user
		new.save()

admin.site.register(New, NewAdmin)
