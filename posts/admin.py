from django.contrib import admin
from .models import Post

# Register your models here.
class imageAdmin(admin.ModelAdmin):
    # tells django admin to display contents in dashboard
    list_display = ['title','photo','alt_text','date_posted','author','last_updated_by']
admin.site.register(Post,imageAdmin)