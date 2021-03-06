from django.contrib import admin
from .models import UserProfile, Category, Article
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'avatar', 'description']

admin.site.register(UserProfile, UserProfileAdmin)


class ArtcleAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content']
    list_display = ['title', 'category', 'created_at']

admin.site.register(Article, ArtcleAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'cover']

admin.site.register(Category, CategoryAdmin)



    

