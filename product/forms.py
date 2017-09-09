from django import forms
from .models import RequiredDataTuple, Client, Product

class BatchForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(BatchForm, self).__init__(*args, **kwargs)

def generateForm(productType):
    dataset = RequiredDataTuple.objects.filter(reqType=productType)
    fields = {}
    for data in dataset:
        if data.fieldType == 'int':
            fields[data.identifier] = forms.IntegerField()
        elif data.fieldType == 'str':
            fields[data.identifier] = forms.CharField(max_length=200)
        elif data.fieldType == 'date':
            fields[data.identifier] = forms.DateField(widget=forms.SelectDateWidget)
        elif data.fieldType == 'datetime':
            fields[data.identifier] = forms.DateTimeField(widget=forms.SplitDateTimeWidget)
        elif data.fieldType == 'Product':
            choices =[]
            for product in Product.objects.filter(productType=data.productType):
                choices.append((product,str(product)))
            fields[data.identifier]=forms.ChoiceField(choices)
        elif data.fieldType == 'Client':
            choices = []
            for client in Client.objects.filter(clientType=data.clientType):
                choices.append((client,str(client)))
            fields[data.identifier]=forms.ChoiceField(choices)

    return type('BatchForm', (forms.Form,), fields)



