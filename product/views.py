# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from . import models
from . import forms
from .blockchain.bigchain_connector import BlockChain

def index(request):
    return HttpResponse("Success")

def submit(request,pk):
    if request.method == 'POST':
        data = request.POST.dict()
        del data['csrfmiddlewaretoken']
        entry = models.BatchEntry()
        entry.batch = data['Batch ID']
        entry.product_id = pk
        db = BlockChain()
        handle = db.write({'data':data})
        entry.key = handle.get('id')
        entry.save()
        return HttpResponseRedirect(reverse('product:batch',args=[entry.key]))
    product = get_object_or_404(models.Product,pk=pk)
    productType = models.ProductType.objects.get(pk=product.productType.pk)
    form = forms.generateForm(productType)
    return render(request, 'submit.html', context={'form':form,'product':product})


def batch(request,pk):
    db= BlockChain()
    transaction = db.get_tx(key=pk)
    entry = models.BatchEntry.objects.get(key=pk)
    product = get_object_or_404(models.Product, pk=entry.product_id)
    data = transaction['asset']['data']
    keyValueList = []
    for key in data:
        li = str(key)+'  :   '+str(data[key])
        keyValueList.append(li)
    print(keyValueList)

    return render(request, 'batch.html', context={'batch':keyValueList, 'product':product})

def client(request,pk):
    client = get_object_or_404(models.Client, pk=pk)
    products = models.Product.objects.filter(client=client)
    return render(request, 'client.html', context={'client':client,'products':products})



