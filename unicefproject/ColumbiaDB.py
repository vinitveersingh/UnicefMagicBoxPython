import os
import pandas as pd
import pdb
from datetime import datetime, timedelta

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "unicefproject.settings")

import django
django.setup()

from magicbox.models import ProviderAndCountry, ColumbiaData

if __name__ == '__main__':
    path_csv = 'data/acme/'
    csv_files = []
    for filename in os.listdir(path_csv):
        file = os.path.join(path_csv , filename)
        csv = pd.read_csv(open(file, 'r'))
        col_id_origin = csv.columns.values[0]
        col_id_destination = csv.columns.values[1]
        col_journeys = csv.columns.values[2]
        col_people = csv.columns.values[3]

        for index,row in csv.iterrows():
            country, country_code, admin1_from, admin2_from, shapefile = row[col_id_origin].split('_')
            country, country_code, admin1_to, admin2_to, shapefile = row[col_id_destination].split('_')
            date = a = datetime.strptime(filename.replace('.csv', ''), "%Y-%m-%d").date()
            created_at = datetime.now().date()
            updated_at = created_at
            provider_object = ProviderAndCountry.objects.get(country_code = country_code )
            journeys = row[col_journeys]
            people = row[col_people]
            print(col_journeys)
            print(row['journeys'])
            dict = {}
            dict['provider_country'] = provider_object
            dict['date'] = date
            dict['created_at'] = created_at
            dict['updated_at'] = updated_at
            dict['id_origin'] = admin2_from
            dict['id_destination'] = admin2_to
            dict['journeys'] = journeys
            dict['people'] = people
            dict['shapefile'] = shapefile
            #print(dict)
            columbia_obj = ColumbiaData(**dict)
            columbia_obj.save()
