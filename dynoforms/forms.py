from django import forms
from dynoforms.models import Entry

FIELDS = {
    'string': forms.CharField,
    'integer': forms.IntegerField,
    'float': forms.FloatField,
    'boolean': forms.BooleanField,
    'date': forms.DateField,
    'email': forms.EmailField,
}


class DynoForm(forms.ModelForm):

    class Meta(object):
        model = Entry
        fields = []

    def __init__(self, **kwargs):
        self.schema = kwargs.pop('schema')
        super(DynoForm, self).__init__(**kwargs)
        for field in self.schema.fields.keys():
            try:
                self.fields[field] = FIELDS[self.schema.fields[field].pop('type')]()
            except KeyError:
                self.errors[field] = ["Type {} isn't supported.".format(
                    self.schema.fields[field]['type'])]

    def save(self, commit=True):
        self.instance.schema = self.schema
        self.instance.data = self.cleaned_data
        self.instance.save()
        return self.instance
