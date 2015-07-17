from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404
from dynoforms.models import Schema, Entry
from dynoforms.forms import DynoForm


class Schemes(ListView):
    model = Schema
    template_name = 'dynoforms/schemes.html'
    context_object_name = 'schemes'


class EntryDetail(DetailView):
    model = Entry
    tempalte_name = 'dynoforms/entry_detail.html'


class NewEntry(CreateView):
    model = Entry
    form_class = DynoForm
    template_name = 'dynoforms/form.html'

    def get_context_data(self, **kwargs):
        context = {}
        context['schema'] = get_object_or_404(Schema, pk=self.kwargs['pk'])
        context.update(kwargs)
        return super(NewEntry, self).get_context_data(**context)

    def get_form_kwargs(self):
        kwargs = super(NewEntry, self).get_form_kwargs()
        if self.kwargs['pk']:
            kwargs.update({'schema': get_object_or_404(
                Schema, pk=self.kwargs['pk'])
            })
        kwargs['owner'] = self.request.user
        return kwargs
