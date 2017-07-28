# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Species(models.Model):
    """ Class to represent a specific Lactarius mushroom

        Note: if adding more families, make this a superclass
        so that inheriting species can have different fields """
    scientific_name = models.CharField(max_length=100,
            verbose_name = "Scientific Name", default='')
    cap_color = models.CharField(max_length=40,
            verbose_name = "Cap color", default='')
    cap_zoned = models.CharField(max_length=40,
            verbose_name = "Cap zoned", default='')
    cap_texture = models.CharField(max_length=40,
            verbose_name = "Cap texture", default='')
    cap_margin = models.CharField(max_length=40,
            verbose_name = "Cap margin when mature", default='')
    cap_center = models.CharField(max_length=40,
            verbose_name = "Cap center when mature", default='')
    gill_color = models.CharField(max_length=40,
            verbose_name = "Gill color", default='')
    gill_attachment = models.CharField(max_length=40,
            verbose_name = "Gill attachment", default='')
    gill_spacing = models.CharField(max_length=40,
            verbose_name = "Gill spacing", default='')
    latex_color = models.CharField(max_length=40,
            verbose_name = "Latex color", default='')
    latex_stains_gills = models.CharField(max_length=40,
            verbose_name = "Latex stains gills", default='')
    latex_changes_color = models.CharField(max_length=40,
            verbose_name = "Latex changes color when dry", default='')
    stipe_color = models.CharField(max_length=40,
            verbose_name = "Stipe color", default='')
    stipe_texture = models.CharField(max_length=40,
            verbose_name = "Stipe texture", default='')
    flesh_color = models.CharField(max_length=40,
            verbose_name = "Flesh color", default='')
    flesh_changes_color = models.CharField(max_length=40,
            verbose_name = "Flesh changes color when sliced", default='')
    spore_color = models.CharField(max_length=40,
            verbose_name = "Spore color", default='')
    odor = models.CharField(max_length=40,
            verbose_name = "Odor", default='')
    taste = models.CharField(max_length=40,
            verbose_name = "Taste", default='')

    def attrs(self):
        """ Generator for (field_name, data) pairs """
        for field in self._meta.fields:
            if field.name not in ["id", "scientific_name"]:
                yield field.verbose_name, getattr(self, field.name)

    @classmethod
    def get_fields(cls): 
        """ Generator for all Field objects in the class """   
        for field in cls._meta.fields:
            if field.name not in ["id", "scientific_name"]:
                yield field

    def __str__(self): 
        """ The string representation of the species is its scientific name """
        return self.scientific_name


