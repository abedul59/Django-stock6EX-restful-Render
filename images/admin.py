from django.contrib import admin

# Register your models here.
from images import models
from images.models import Images
from images.models import  Stock6Sign202212, Stock6Sign202304, Stock6Sign202308, Stock6Sign202309, Stock6Sign202310, Stock6Sign202311, Stock6Sign202312
admin.site.register(models.Images)
admin.site.register(models.Stock6Sign202212)
admin.site.register(models.Stock6Sign202304)
admin.site.register(models.Stock6Sign202308)
admin.site.register(models.Stock6Sign202309)
admin.site.register(models.Stock6Sign202310)
admin.site.register(models.Stock6Sign202311)
admin.site.register(models.Stock6Sign202312)