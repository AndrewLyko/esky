from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView, TemplateView

from search.forms import SearchForm


class SearchView(TemplateView):
    template_name = 'search/search.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form'] = SearchForm(self.request.GET) if self.request.GET else SearchForm()
        return ctx

    def get(self, request, *args, **kwargs):
        form = SearchForm(request.GET)

        if form.is_valid():
            return redirect(reverse('search:flights') + request.get_full_path()[1:])

        return super().get(request, *args, **kwargs)


class ResultsView(TemplateView):
    template_name = 'search/results.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form'] = SearchForm(self.request.GET) if self.request.GET else SearchForm()
        return ctx


class ResultsAjaxView(TemplateView):
    template_name = 'search/results_ajax.html'
