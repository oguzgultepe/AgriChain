# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Industry(models.Model):
    title = models.CharField(max_length=30)
    def __str__(self):
        return self.title

class ClientType(models.Model):
    title = models.CharField(max_length=30)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Client(models.Model):
    title = models.CharField(max_length=30)
    clientType = models.ForeignKey(ClientType, on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class ProductType(models.Model):
    title = models.CharField(max_length=50)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=30)
    productType = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.title

class RequiredDataTuple(models.Model):
    reqType = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name='required')
    identifier = models.CharField(max_length=30)
    fieldType = models.CharField(max_length=30)
    #fieldType is a choicefield in forms
    #productType/clientType appears on forms if fieldtype is set as product/client
    productType = models.ForeignKey(ProductType, null=True, blank=True)
    clientType= models.ForeignKey(ClientType, null=True, blank=True)

class BatchEntry(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, editable=False)
    batch = models.CharField(max_length=100, editable=False)
    key = models.CharField(max_length=300, editable=False)

