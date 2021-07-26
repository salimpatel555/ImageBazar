from django.contrib import admin
from .models import Category,Image
# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title','description','image','added_date','category']
admin.site.register(Category)
admin.site.register(Image,ImageAdmin)

