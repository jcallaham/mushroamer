# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic
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

