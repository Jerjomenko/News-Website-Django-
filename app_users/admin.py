from django.contrib import admin
from .models import News, Profile

class NewsAdmin(admin.ModelAdmin):
    list_display = ["title", "created", "update", "author"]


class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ["user", "city", "tel", "verify", "moderator" ]


admin.site.register(News, NewsAdmin)
admin.site.register(Profile, ProfileAdmin)


