from django.contrib import admin
from .models import Post

# Register your models here.
class imageAdmin(admin.ModelAdmin):
    # tells django admin to display contents in dashboard
    list_display = ['id','photo','alt_text','date_posted','author','last_updated_by','tags','suggested_tags','suggested_alt_text','uuid','approved']
admin.site.register(Post,imageAdmin)