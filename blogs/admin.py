from django.contrib import admin

from .models import Blog
# Register your models here.
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
	list_display = ('title', 'created', 'show_tags', 'user')
	fields = ['title', 'text', 'image', 'tags']

	def show_tags(self, obj):
		tags = obj.tags.names()
		return ",".join(tags)

	def save_model(self, request, blog, form, change):
		blog.user = request.user
		blog.save()

admin.site.register(Blog, BlogAdmin)