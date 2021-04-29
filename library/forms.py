from django import forms
from .models import Collection,CollectionBook,Book




class CollectionForm(forms.ModelForm): 
    
    class Meta: 
        model = Collection 
        fields = ["name"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super(CollectionForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            if not key=='user':
                self.fields[key].required = True
            self.fields[key].widget.attrs['class'] = 'form-control'


    def save(self, commit=True):
        instance = super(CollectionForm, self).save(commit=False)
        instance.name = self.cleaned_data['name']
        instance.user = self.user
        if commit:
            instance.save()
        return instance


class CollectionBookForm(forms.ModelForm):
    class Meta: 
        model = CollectionBook
        fields = ["book"]

    def __init__(self, *args, **kwargs):
        self.collection = kwargs.pop("collection")
        super(CollectionBookForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            if not key=='collection':
                self.fields[key].required = True
            self.fields[key].widget.attrs['class'] = 'form-control'


    def save(self, commit=True):
        instance = super(CollectionBookForm, self).save(commit=False)
        instance.book = self.cleaned_data['book']
        instance.collection = self.collection
        if commit:
            instance.save()
        return instance
