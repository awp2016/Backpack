from django.contrib import admin

from . import models


# Register your models here.
admin.site.register(models.Destination)
admin.site.register(models.Comment)
admin.site.register(models.UserProfile)
admin.site.register(models.Review)
admin.site.register(models.Wishlist)

