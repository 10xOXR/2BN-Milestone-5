from django.contrib import admin
from users.models import Profile, Badges, BadgeType

admin.site.register(Profile)
admin.site.register(Badges)
admin.site.register(BadgeType)
