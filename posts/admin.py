from django.contrib import admin
from .models import Post

# Register your models here.
class imageAdmin(admin.ModelAdmin):
    # tells django admin to display contents in dashboard
    list_display = ['title','photo','altText']
admin.site.register(Post,imageAdmin)