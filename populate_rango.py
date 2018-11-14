import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
import random

django.setup()

from rango.models import Category, Page

def populate():
    python_pages = [
        {'title': 'Offical Python Tutorial',
         'url': 'http://docs.python.org/2/tutorial/'},
        {'title': 'How to think like a Computer Scientist',
         'url': 'Http://www.greenteapress.com/thinkpython/'},
        {'title': 'Learn Python in 10 minutes',
         'url': 'Http://www.korokithakis.net/tutorials/python/'} ]

    django_pages = [
        {'title': 'Offical Django Tutorial',
         'url': 'http://doc.djangoproject.com/en/1.9/intro/tutorial01/'},
        {'title': 'Django Rocks',
         'url': 'http://www.djangorocks.com/'},
        {'title': 'How to Tango with Django',
         'url': 'http://www.tangowithdjango.com/'} ]

    other_pages = [
        {'title': 'Bottle',
         'url': 'http://bottlepy.org/docs/dev/'},
        {'title': 'Flask',
         'url': 'http://flask.pocoo.org/'} ]

    cats = {'Python': {'pages': python_pages},
            'Django': {'pages': django_pages},
            'Other Frameworks': {'pages': other_pages} }

    for cat, cat_data in cats.items():
        c= add_cat(cat)
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print('- {0} - {1}'.format(str(c), str(p)))

def add_page(cat, title, url):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = random.randint(1,200)
    p.save()
    return p

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    if c.name == 'Python':
        c.views = 128
        c.likes = 64
    if c.name == 'Django':
        c.views = 64
        c.likes = 32
    if c.name == 'Other Frameworks':
        c.views = 32
        c.likes = 16
    c.save()
    return c

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
