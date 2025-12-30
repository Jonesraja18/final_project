from django.contrib import admin
from base.models import Category,Articles
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','category_name','created_at','updated_at']


class ArticlesAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','category','updated_at','status','is_treanding']

    prepopulated_fields={
        'slug':('title',)
    }
admin.site.register(Category,CategoryAdmin)
admin.site.register(Articles,ArticlesAdmin)
