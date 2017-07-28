# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from sieve.forms import QueryForm
from django.views.generic.edit import FormView
import sieve_functions as sf
from encyclopedia.models import Species



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
        return render(request, 'results.html', {'search_results':search_results[:5]} )

    else:
        """ Form has not been completed: generate a new form """
        form = QueryForm(field_dict)
        return render(request, 'query.html', {'form': form})

