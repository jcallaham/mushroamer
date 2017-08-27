# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic
from sieve.forms import QueryForm
from django.views.generic.edit import FormView
import sieve_functions as sf
from .models import Species

class IndexView(generic.ListView):
    template_name = 'encyclopedia/index.html'
    context_object_name = 'species_list'

    def get_queryset(self):
        """Returns a list of all species. Used to populate encyclopedia index.
            (I think this is an override) """
        return Species.objects.order_by('scientific_name')


class DetailView(generic.DetailView):
    model = Species
    template_name = 'encyclopedia/detail.html'


def query(request):

    # Create a dictionary of all possible choices for fields using external function
    field_dict = sf.get_choices()    # Keys are fields, entries are all choices in database

    if request.method == 'POST':
        """ Form is complete: process data 
        request.POST is a dictionary indexed by field 'name' and with entries as the selected choice
        If no choice was selected, the entry is ''
        """
        # Use external function to find percent match between query and species
        search_results = sf.search(field_dict, request.POST)   # Two-ples of (species, pct_match), sorted descending

        # Show best 5 matches
        return render(request, 'sieve/results.html', {'search_results':search_results[:5]} )

    else:
        """ Form has not been completed: generate a new form """
        form = QueryForm(field_dict)
        return render(request, 'sieve/query.html', {'form': form})

