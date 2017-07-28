from django import forms

class QueryForm(forms.Form):
    """ Form used to query in sieve app. Needs to be defined so that
            the variable number of fields with variable content can be
            custom loaded from the database """

    def __init__(self, field_dict, *args, **kwargs):
        super(QueryForm, self).__init__(*args, **kwargs)
        
        # Add variable number of fields to dictionary of fields
        for field in field_dict.keys():
            self.fields[field.name] = forms.ChoiceField( choices=field_dict[field], required=False )

