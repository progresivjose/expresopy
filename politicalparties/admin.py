from django.contrib import admin
from .models import PoliticalParty
# Register your models here.

class PoliticalPartyAdmin(admin.ModelAdmin):
	list_display = ('name', 'created')
	fields       = ['name']

	def save_model(self, request, politicalparty, form, change):
		politicalparty.user = request.user
		politicalparty.save()

admin.site.register(PoliticalParty, PoliticalPartyAdmin)