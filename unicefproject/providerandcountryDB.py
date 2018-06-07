import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "unicefproject.settings")

import django
django.setup()

from magicbox.models import ProviderAndCountry

def insert(*kwargs):
    obj = ProviderAndCountry(**dict)
    obj.save()
    print('Done')




if __name__ == '__main__':
    # dict = {}
    # dict['provider'] = 'acme'
    # dict['country'] = 'Columbia'
    # dict['country_code'] = '0'
    # insert(dict )

    dict = {}
    dict['provider'] = 'worldpop'
    dict['country'] = 'Democratic Republic of the Congo'
    dict['country_code'] = '63'
    insert(dict )
