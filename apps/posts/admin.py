from django.contrib import admin
from .models import Post, Image


class ImageInline(admin.TabularInline):
    model = Image
    extra = 3


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {
                'fields':[
                    'content',
                ]
            }
        )
    ]
    inlines = [ImageInline]
    list_display = ('content',)


admin.site.register(Post, PostAdmin)
