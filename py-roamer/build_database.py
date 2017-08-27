""" Create Cloud SQL Database from csv file 

Note: If the old database isn't cleared first, this could
    result in duplicate entries. Run rebuild.sh to flush
    old database and prepare a new one using manage.py """

import django
django.setup()  # Needs to be done before importing Species model

from sieve.models import Species


def create_database():
    """ Create database from csv file, if script called directly
        Note that column-character relationships have to be specified manually
    """

    import csv
    csv_file="data/lactarius.csv"      # Path to .csv data file

    dataReader = csv.reader(open(csv_file), delimiter=',')
    next(dataReader)   # Skip header row with data titles

    for row in dataReader:
        species = Species()  # Create object

        # Save csv data for this species
        print(row[0])
        species.scientific_name = row[0]
        species.cap_color = row[1]
        species.cap_texture = row[2]
        species.cap_zoned = row[3]
        species.cap_margin = row[4]
        species.cap_center = row[5]
        species.gill_color = row[6]
        species.gill_attachment = row[7]
        species.gill_spacing = row[8]
        species.latex_color = row[9]
        species.latex_stains_gills = row[10]
        species.latex_changes_color = row[11]
        species.stipe_color = row[12]
        species.stipe_texture = row[13]
        species.flesh_color = row[14]
        species.flesh_changes_color = row[15]
        species.spore_color = row[16]
        species.odor = row[17]
        species.taste = row[18]


        # Commit to database. Database details are specified in settings.py
        species.save()  

    
if __name__ == '__main__':
    create_database()
