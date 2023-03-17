from django.contrib import admin
from . models import (
    UserProfile,
    # ContactProfile,
    # Testimonial,
    Media,
    # Portfolio,
    Blog,
    # Certificate,
    # Skill,
    # finprog
    )


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'user')

# @admin.register(ContactProfile)
# class ContactAdmin(admin.ModelAdmin):
# 	list_display = ('id', 'timestamp', 'name',)

# @admin.register(Testimonial)
# class TestimonialAdmin(admin.ModelAdmin):
#     list_display = ('id','name','is_active')

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

# @admin.register(Portfolio)
# class PortfolioAdmin(admin.ModelAdmin):
#     list_display = ('id','name','is_active')
#     readonly_fields = ('slug',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active')
    readonly_fields = ('slug',)


from django.db import models

class CodeSnippet(models.Model):
    title = models.CharField(max_length=100)
    code = models.TextField()

    def __str__(self):
        return self.title
