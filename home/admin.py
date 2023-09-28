
# Register your models here.
from django.contrib import admin
from .models import Post,Contact,Category,Friendes,Comment
admin.site.register(Contact)
admin.site.register(Category)
admin.site.register(Friendes)
admin.site.register(Comment)

@admin.register(Post)
class NewAdmin(admin.ModelAdmin):
    list_display=['id', 'name', ]
    search_fields=[ 'name']
