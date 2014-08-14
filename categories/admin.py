from django.contrib import admin
from .models import Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('title', 'created', 'user', 'category')
	fields       = ['title', 'category']

	def save_model(self, request, category, form, change):
		category.user = request.user
		category.save()

admin.site.register(Category, CategoryAdmin)