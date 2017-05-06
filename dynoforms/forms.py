from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
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
    '''
    A form created dynamically based on fields from a Schema object.
    '''

    class Meta(object):
        model = Entry
        fields = []

    def __init__(self, **kwargs):
        # pop some kwargs because the form didn't expect them.
        self.schema = kwargs.pop('schema')
        self.owner = kwargs.pop('owner')
        super(DynoForm, self).__init__(**kwargs)
        for field in self.schema.fields.keys():
            # pop the field type, leaving only paramenters
            ftype = self.schema.fields[field].pop('type')
            try:
                self.fields[field] = FIELDS[ftype]()  # Instantiate the field.
            except KeyError:
                self.add_error(
                    field,
                    ValidationError(
                        _("Type {} isn't supported.".format(ftype)),
                        code='invalid'
                    )
                )

    def save(self, commit=True):
        self.instance.schema = self.schema
        self.instance.owner = self.owner
        self.instance.data = self.cleaned_data
        self.instance.save()
        return self.instance
