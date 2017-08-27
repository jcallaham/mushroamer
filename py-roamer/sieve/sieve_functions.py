# Functions to help views.py relate to the lactarius database
from .models import Species


def get_choices():
    """ Return a dictionary of all fields in the Species model
    as keys, with the unique choices as a list of strings
        Used to populate the search form. """
    field_dict = {}

    for field in Species.get_fields():
        unique_choices = Species.objects.order_by().values_list(field.name, flat=True).distinct()
        field_dict[field] = [('', '')] + zip(unique_choices, unique_choices)  # First term is for default (blank)

    return field_dict



def match(query, species):
    """ Return percent match between query and this species, for fields given in query """
    
    # Number of fields where selection matches species
    matches = sum( [ getattr(species, field.name) == query[field] for field in query.keys() ] )

    # Return percent match
    return matches*100 / len(query)



def search(field_dict, post_query):
    """ Read POST form to get choices for selected fields and match selected fields to
            species in database.
        Return a list of tuples, where the first entry is a species ID and the second is a match pct.
            The list is sorted in descending order, so search_results[:5] gives the best five matches
    """ 
    # Pull out choices from query form, keeping only selected fields
    form_data = { field: post_query[field.name] for field in field_dict.keys() if post_query[field.name] != '' }

    # Loop through all species and calculate match percentages
    search_results = [ ( species, match(form_data, species) ) for species in Species.objects.all() ]

    # Sort by match percentage in descending order
    search_results.sort( reverse=True, key = lambda entry: entry[1] )
  
    return   search_results
