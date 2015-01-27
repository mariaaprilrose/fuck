from django.contrib import admin
from blog.models import Blog

class BlogAdmin(admin.ModelAdmin):
	list_display = ('title', 'date_published')
	list_filter = ['date_published']
	date_hierarchy = 'date_published'
	search_fields = ['title']

admin.site.register(Blog, BlogAdmin)