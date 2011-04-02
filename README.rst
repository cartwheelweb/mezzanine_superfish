===================
Mezzanine Superfish
===================

By Audrey Roy with Daniel Greenfeld assisting

**Note**: Still alpha. Use with caution until formal release

Installation
============

Do the following::

    pip install mezzanine_superfish
    
Or::

    pip install -e git+git@github.com/cartwheelweb/mezzanine_superfish.git#egg=mezzanine_superfish

Fetch the static media::

    python manage.py collectstatic

Usage
=====

In the `templates/base.html` file of your Mezzanine project add the following::

    {% load mezzanine_superfish_tags %}

Replace::

    {% page_menu "pages/menus/primary.html" %}
    
with::

    {% superfish_submenu "mezzanine_superfish/superfish.html" %}
