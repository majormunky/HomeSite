from django.contrib import admin
from home import models


admin.site.register(models.BlogCategory)
admin.site.register(models.BlogPost)
admin.site.register(models.BlogImage)
