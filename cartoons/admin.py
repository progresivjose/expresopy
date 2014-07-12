from django.contrib import admin
from .models import Cartoon
from sorl.thumbnail import get_thumbnail
# Register your models here.
class CartoonAdmin(admin.ModelAdmin):
	list_display = ('title', 'created', 'image')
	#list_display = ('title', 'created')

	def image_cartoon(self, obj):
		return '<img src="%s" />' % get_thumbnail(obj.image, '50x100', format='PNG').url

	image_cartoon.allow_tags = True

admin.site.register(Cartoon, CartoonAdmin)