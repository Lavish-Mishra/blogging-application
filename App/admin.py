from django.contrib import admin
from .models import Post

# Register your models here.
#admin.site.register(Post)
admin.site.site_header = "Custom Admin Project"

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author', 'date_posted')
    fieldsets = (
        (None, {
            'fields' : ('title','content','date_posted','author')
            }),
        ('Additional Information', {
            'classes' : ('collapse',),
            'fields': ('likes',)
        }))