from django.contrib import admin

from blog.models import Post

# Register your models here.

# admin.site.register(Post)
@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    # para generar el slug automaticamente
    prepopulated_fields = {'slug': ('title',)}
    # Que se busque y coloque el id del author.
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    # mostrar cantidad de posto por filtro
    show_facets = admin.ShowFacets.ALWAYS
    
    