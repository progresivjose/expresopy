from django.contrib import admin
from .models import Politic
from politicentities.models import PoliticEntity
from politicfiles.models import PoliticFile
# Register your models here.

class PoliticEntityInLine(admin.StackedInline):
	model  = PoliticEntity
	fields = ['entity', 'role','current', 'description']
	extra  = 1

class PoliticFileInLine(admin.StackedInline):
	model  = PoliticFile
	fields = ['file']
	extra  = 1

class PoliticAdmin(admin.ModelAdmin):
	list_display = ('firstname', 'lastname', 'political_party', 'ranking','created', 'user')
	inlines      = [PoliticEntityInLine, PoliticFileInLine]
	fields       = ['firstname', 'lastname', 'political_party', 'degree','biography', 'image']

	def save_model(self, request, politic, form, change):
		politic.user = request.user
		politic.save()

admin.site.register(Politic, PoliticAdmin)
