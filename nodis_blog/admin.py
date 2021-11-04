from django.contrib import admin

from .models import Post,Tag

# Register your models created in models.py here.

#---------------------------------------
# Regsiter the Post Model
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','status','created_on')
    list_filter = ('status',)
    search_fields = ['title','content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post,PostAdmin)
#---------------------------------
# Regsiter the Tag Model
admin.site.register(Tag)
#--------------------------
# Regsiter the Profile Model
##admin.site.register(Profile)