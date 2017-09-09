# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from . import models
from . import forms
# Create your views here.
##TODO create views for product instance creation

def index(request):
    return HttpResponse("Success")

def submit(request,pk):
    if request.method == 'POST':
        data = request.Post.dict()
        return HttpResponseRedirect(reverse('product:submit'))
    product = get_object_or_404(models.Product,pk=pk)
    productType = models.ProductType.objects.get(pk=product.productType.pk)
    form = forms.generateForm(productType)
    return render(request, 'submit.html', context={'form':form,'pk':pk})
