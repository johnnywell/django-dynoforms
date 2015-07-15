from django.views.generic import ListView, DetailView, CreateView, FormView
from dynoforms.models import Schema, Entry
from dynoforms.forms import DynoForm


class DynoFormList(ListView):
    model = Schema


class DynoFormEntryDetail(DetailView):
    model = Entry
    tempalte_name = 'dynoforms/entry_detail.html'


class DynoFormCreateData(CreateView):
    model = Entry
    form_class = DynoForm
    template_name = 'dynoforms/form.html'

    def get_form_kwargs(self):
        kwargs = super(DynoFormCreateData, self).get_form_kwargs()
        if self.kwargs['schema_pk']:
            kwargs.update({'schema': Schema.objects.get(
                id=self.kwargs['schema_pk'])
            })
        return kwargs
