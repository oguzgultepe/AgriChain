# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from . import models

##TODO set modeladmins for easy use of models


class DataTupleInline(admin.StackedInline):
    model = models.RequiredDataTuple
    fk_name= 'reqType'
    extra = 4

class ProductTypeAdmin(admin.ModelAdmin):
    inlines= [DataTupleInline]


admin.site.register(models.Industry)
admin.site.register(models.Client)
admin.site.register(models.ClientType)
admin.site.register(models.ProductType,ProductTypeAdmin)
admin.site.register(models.Product)



