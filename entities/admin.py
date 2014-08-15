from django.contrib import admin
from .models import Entity, EntityType
# Register your models here.

class EntityTypeAdmin(admin.ModelAdmin):
	list_display = ('name', 'created')
	fields       = ['name']

	def save_model(self, request, entitytype, form, change):
		entitytype.user = request.user
		entitytype.save()

class EntityAdmin(admin.ModelAdmin):
	list_display = ('name', 'entitytype', 'created')
	fields = ['name', 'entitytype']

	def save_model(self, request, entity, form, change):
		entity.user = request.user
		entity.save()

admin.site.register(EntityType, EntityTypeAdmin)
admin.site.register(Entity, EntityAdmin)